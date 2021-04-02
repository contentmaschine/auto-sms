import morse
import simon_says
import wires
import concurrent.futures

# TODO:
#  auto-sms configure for actual task
#  game_master implementation
#  LCD
#  Success LEDS for SimonSays and Wires

# game should start with SimonSays and Wires active, which need to be solved to enable morse, which then enables sms defusing

executor = concurrent.futures.ThreadPoolExecutor()
simon_says_result = executor.submit(simon_says.simon_says).result()
wires_result = executor.submit(wires.wires).result()

if simon_says_result and wires_result:
    print("first stage check")


# the pins are 5, 6, 26 from left to right

