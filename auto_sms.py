import serial
import time
import re

rgx_index = re.compile("([0-9]+)")
rgx_number = re.compile("(\+[0-9]+)")

port = serial.Serial("/dev/serial0", baudrate=115000, timeout=10.0)
enter = b"\n"
done = False

port.write(b"AT+CPIN=2401" + enter)
time.sleep(0.3)
if port.read(10).decode("utf-8") == "ERROR":
    raise ValueError("CAN'T ENTER PIN")

# Disable Echo
port.write(b'ATE0' + enter)
time.sleep(0.3)

# clear any misleading bytes in the buffer
port.reset_output_buffer()


def send_message(sms_index):
    port.write(b"AT+CMGF=1" + enter)
    time.sleep(1)
    port.write(b"AT+CMGR=" + sms_index + enter)
    time.sleep(1)
    sms = port.read(1000)
    sms = sms.decode("utf-8")
    time.sleep(1)

    print("sms:")
    print(sms)

    match_object = rgx_number.search(sms)
    if match_object is None:
        raise RuntimeError("Cannot read sms")
    number = match_object.group()

    print("sending sms to number: ")
    print(number)

    number = str.encode(number)
    port.write(b"AT+CMGS=\"" + number + b"\"" + enter)
    time.sleep(0.5)
    port.write(b"This is an automated return message, sent to impress.")
    time.sleep(0.1)
    port.write(b"\x1A")

    done = True


while not done:
    event = port.read(100)
    # port outputs bytes, regex needs string, commands need bytes
    event = event.decode("utf-8")
    print(event)
    match_object = rgx_index.search(event)
    if match_object is not None:
        sms_index = match_object.group()
        print("Received SMS at Index: " + sms_index)
        sms_index = str.encode(sms_index)
        send_message(sms_index)
    time.sleep(1)
