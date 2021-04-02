import random
import time
import game_state
from gpiozero import RGBLED, Button, Device
from colorzero import Color

# for testing
#from gpiozero.pins.mock import MockFactory, MockPWMPin
#Device.pin_factory = MockFactory(pin_class=MockPWMPin)

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

# cycle_max = how many colors need to be correctly processed until success
# wait_time = how long
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

cycles = 1

# sends command to RGBLED every cycle
def blink():
    for color in pattern:
        led.color = Color(color)
        time.sleep(1)
        led.off()
        time.sleep(0.5)

# function to break loop when correct button is pressed
def right_button_pressed():
    global pressed
    pressed = True

# main function
def simon_says():
    global cycles
    global pressed

    # loops through n cycles, always adding random colors the pattern
    while cycles <= cycle_max:
        random_color = random.choice(colors)
        pattern.append(random_color)
        blink()

        # expects a response for every shown color
        for color in pattern:

            start_time = time.clock()
            pressed = False

            current_chiffre = chiffre_list[game_state.strike_counter]
            right_button = current_chiffre[color]

            right_button.when_activated = right_button_pressed

            wrong_buttons = buttons.copy()
            wrong_buttons.remove(right_button)

            # calls the strike function when of the 3 wrong buttons is pushed
            for wrong_button in wrong_buttons:
                wrong_button.when_activated = game_state.strike

            #watches the buttons continually and breaks the loop when correctly chosen
            while not pressed:

                # if no response for x seconds, then repeat the pattern and reset the timer
                if (time.clock() - start_time) >= wait_time:
                    blink()
                    start_time = time.clock()

        led.on()
        time.sleep(1)
        led.off()
        time.sleep(1)

        cycles += 1

    game_state.simon_says_done = True
