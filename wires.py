from gpiozero import DigitalInputDevice
import game_state


right_pin = 27
wrong_pin = 17

right_connection = DigitalInputDevice(pin=right_pin, pull_up=True)
wrong_connection = DigitalInputDevice(pin=wrong_pin, pull_up=True)

def wires():
    right_pin = 27
    wrong_pin = 17

    right_connection = DigitalInputDevice(pin=right_pin, pull_up=True)
    wrong_connection = DigitalInputDevice(pin=wrong_pin, pull_up=True)

    right_connection.when_deactivated = right_wire
    wrong_connection.when_deactivated = game_state.strike

def right_wire():
    game_state.success(16)
    game_state.wires_done = True


