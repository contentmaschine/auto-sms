import serial
import time

while True:
        msg = port.readlines()
        print(msg)
        time.sleep(0.2)

