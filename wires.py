import gpiozero as gpio0
import time

right_wires_connected = gpio0.Button(0).is_pressed

while True:
    if right_wires_connected is False:
        print("STRIKE!")
    time.sleep(1)