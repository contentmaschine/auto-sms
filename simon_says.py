import random
import time
import game_state
from gpiozero import RGBLED, Button, Device
from colorzero import Color
from signal import pause

# for testing
#from gpiozero.pins.mock import MockFactory
#Device.pin_factory = MockFactory()


# RGBLED has three inputs
red_pin = 11
green_pin = 10
blue_pin = 9
led = RGBLED(red=red_pin, green=green_pin, blue=blue_pin)

# four different pins watching over four buttons
red_button = Button(12)
green_button = Button(20)
blue_button = Button(1)
yellow_button = Button(16)

buttons = [red_button, green_button, blue_button, yellow_button]

cycle_max = 4
wait_time = 7

# pattern list will store the colors seen by the player
colors = ["red", "blue", "yellow", "green"]
pattern = []

# extra rules from the manual, the chiffre changes depending on strike_count
zero_strike_dict = {"red": blue_button, "blue": red_button, "green": yellow_button, "yellow": green_button}
one_strike_dict = {"red": yellow_button, "blue": green_button, "green": blue_button, "yellow": red_button}
two_strike_dict = {"red": green_button, "blue": red_button, "green": yellow_button, "yellow": blue_button}

chiffre_list = [zero_strike_dict, one_strike_dict, two_strike_dict]
current_chiffre = chiffre_list[game_state.strike_counter]

cycles = 1


# here the colors get encoded to RGBLED terms
def encode_color(color: str):
    if color == "red":
        color_code = (1, 0, 0)
    elif color == "blue":
        color_code = (0, 0, 1)
    elif color == "green":
        color_code = (0, 1, 0)
    elif color == "yellow":
        color_code = (1, 1, 0)
    return color_code


# sends command to RGBLED every cycle
def blink():
    for color in pattern:
        led.color = Color(color)
        time.sleep(1)
        led.off()
        time.sleep(0.5)


def test():
    print("Right Button pressed")

# main function
def simon_says():
    global cycles
    # random color gets selected at start

    # loops through n cycles, always adding colors the pattern
    while cycles <= cycle_max:
        random_color = random.choice(colors)
        pattern.append(random_color)
        blink()
        # expects a response for every shown color
        for color in pattern:
            right_button = current_chiffre[color]
            start_time = time.clock()

            right_button.when_activated = test
            # if no response for x seconds, then repeat the pattern and reset the timer
            if (time.clock() - start_time) >= wait_time:
                blink()
                start_time = time.clock()

        led.on()
        time.sleep(1)
        led.off()

        cycles += 1
