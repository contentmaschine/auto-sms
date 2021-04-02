from gpiozero import DigitalInputDevice
import game_state
import time


right_pin = 27
wrong_pin = 17

right_connection = DigitalInputDevice(pin=right_pin, pull_up=True)
wrong_connection = DigitalInputDevice(pin=wrong_pin, pull_up=True)

def wires():
    right_connection.when_deactivated = right_wire
    wrong_connection.when_deactivated = game_state.strike

    while not game_state.wires_done:
        time.sleep(10)

def right_wire():
    #game_state.success(16)
    game_state.wires_done = True


