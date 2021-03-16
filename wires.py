from gpiozero import Button
import time


cut_wires_pin = 27
no_cut_wires_pin = 17

cut_wires_online = Button(cut_wires_pin).is_pressed
no_cut_wires_online = Button(no_cut_wires_pin).is_pressed

while True:
    if not cut_wires_online:
        print("success")
        pass
    if not no_cut_wires_online:
        print("STRIKE")
        pass
    time.sleep(0.1)
