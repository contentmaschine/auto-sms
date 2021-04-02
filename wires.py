from gpiozero import Button
import time
import game_state


cut_wires_pin = 27
no_cut_wires_pin = 17

cut_wires_online = Button(cut_wires_pin).is_pressed
no_cut_wires_online = Button(no_cut_wires_pin).is_pressed

def wires():
    triggered = False
    while True:
        if not cut_wires_online:
            return 1

        if not no_cut_wires_online and not triggered:
            game_state.strike()
            triggered = True
        time.sleep(0.1)
