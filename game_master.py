import game_state, simon_says, wires, sms_reader, morse
import concurrent.futures, time


# TODO:
#  LCD game_master implementation
#  Instructions for Players

# game starts with SimonSays and Wires active, which need to be solved to enable morse, which then enables sms defusing

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    w = executor.submit(wires.wires)
    s = executor.submit(simon_says.simon_says)

    if s.result():
        print("first stage check")
        # artistic pause
        time.sleep(1)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.submit(morse.morse, {5: "SMS", 6: "FELIX", 26: "DEFUSE"})
            executor.submit(sms_reader.sms_reader)
            if game_state.sms_done:
                print("U DO IT")
