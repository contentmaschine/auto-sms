import simon_says
import wires
import sms_reader
import morse
import concurrent.futures
import game_state



# TODO:
#  check if sms_reader works and finally change all the sleeps to smaller values
#  game_master implementation
#  LCD
#  Success LEDS for SimonSays and Wires

# game should start with SimonSays and Wires active, which need to be solved to enable morse, which then enables sms defusing

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.submit(wires.wires)
    executor.submit(simon_says.simon_says)

if game_state.wires_done and game_state.simon_says_done:
    print("first stage check")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(morse.morse, {5: "SMS", 6: "FELIX", 26: "DEFUSE"})
        executor.submit(sms_reader.sms_reader)
    if game_state.sms_done:
        print("U DO IT")
