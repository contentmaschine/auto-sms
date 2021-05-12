import game_state, simon_says, wires, sms_reader, morse
import concurrent.futures, time


# TODO:
#  success screen
#  SMS correct austesten
#  Instructions for Players
#  Board mehr conveniently stecken
#  Simon Says Buttons anmalen

# game starts with SimonSays and Wires active, which need to be solved to enable morse, which then enables sms defusing

with concurrent.futures.ThreadPoolExecutor() as executor:
    wires = executor.submit(wires.wires)
    simon_says = executor.submit(simon_says.simon_says)

    # both threads return True, when done correctly
    if wires.result() and simon_says.result():
        # artistic pause
        time.sleep(1)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.submit(morse.morse, {5: "SMS", 6: "FELIX", 26: "DEFUSE"})
            sms_reader = executor.submit(sms_reader.sms_reader)
            if sms_reader.result():
                print("SUCCESS")
