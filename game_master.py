import morse
import simon_says
import wires
import concurrent.futures
import game_state
import time


# TODO:
#  auto-sms configure for actual task
#  game_master implementation
#  LCD
#  Success LEDS for SimonSays and Wires

# game should start with SimonSays and Wires active, which need to be solved to enable morse, which then enables sms defusing

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.submit(wires.wires)
    executor.submit(simon_says.simon_says)

if game_state.wires_done and game_state.simon_says_done:
    print("first stage check")


# the pins are 5, 6, 26 from left to right

