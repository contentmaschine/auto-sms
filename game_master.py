import game_state, simon_says, wires, sms_reader, morse
import concurrent.futures, time


# TODO:
#  LCD game_master implementation
#  Instructions for Players

# game should start with SimonSays and Wires active, which need to be solved to enable morse, which then enables sms defusing

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(wires.wires)
    executor.submit(simon_says.simon_says)

if game_state.wires_done and game_state.simon_says_done:
    print("first stage check")
    # artistic pause
    time.sleep(1)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(morse.morse, {5: "SMS", 6: "FELIX", 26: "DEFUSE"})
        executor.submit(sms_reader.sms_reader)
    if game_state.sms_done:
        print("U DO IT")
