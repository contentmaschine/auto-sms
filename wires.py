from gpiozero import Button
import time
from game_state import strike


cut_wires_pin = 27
no_cut_wires_pin = 17

cut_wires_online = Button(cut_wires_pin).is_pressed
no_cut_wires_online = Button(no_cut_wires_pin).is_pressed

triggered = False

while True:
    if not cut_wires_online:
        print("success")
        pass
    if not no_cut_wires_online and not triggered:
        strike()
        triggered = True
    time.sleep(0.1)
