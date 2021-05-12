import game_state, simon_says, wires, sms_reader, morse
import concurrent.futures, time
import lcd_assets

# TODO:
#  success screen
#  Instructions for Players
#  Board mehr conveniently stecken
#  Simon Says Buttons anmalen

lcd_assets.start_screen()

# waits for red and blue button to be pushed
#game_state.start_game()

with concurrent.futures.ThreadPoolExecutor() as executor:
    #executor.submit(lcd_assets.countdown(5, 0))
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
                lcd_assets.win_screen()
