import serial
import time
import re

p = re.compile("READY")

nl = b"\n"

port = serial.Serial("/dev/serial0", baudrate=115000, timeout=3)

port.write(b"AT+CPIN?" + nl)

time.sleep(0.1)
output = port.readlines()
ready = p.search(output)

if not ready:
    port.write(b"AT+CPIN=2401" + nl)
    time.sleep(0.5)
    port.write(b"AT+CPIN?" + nl)
    if not ready:
        raise RuntimeError("sim is not unlocked")

time.sleep(0.1)

while True:
        msg = port.readlines()
        print(msg)
        time.sleep(0.2)

