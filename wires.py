import gpiozero
import time

#test2

correct_pin = 17

button = gpiozero.Button(correct_pin)

while True:
    if button.is_pressed:
        print("connected")
    else:
        print("not connected")
    time.sleep(1)
