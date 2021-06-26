import RPi_I2C_driver, multiprocessing, time
import simon_says

rows = [0x80, 0xC0, 0x94, 0xD4]
mylcd = RPi_I2C_driver.lcd()


# functions

def start_screen():
    mylcd.lcd_display_string_pos("KEEP RASPI", 2, 5)
    mylcd.lcd_display_string_pos("TALKING", 3, 6)
    simon_says.blue_button.wait_for_active()
    simon_says.red_button.wait_for_active()
    mylcd.lcd_clear()
    countdown_process.start()
    return countdown_process


def win_screen(countdown_process):
    countdown_process.terminate()
    mylcd.lcd_clear()
    pos_one = [1, 7, 13]
    pos_two = [4, 10, 16]
    x = 0
    while True:
        for pos in pos_one:
            mylcd.lcd_display_string_pos("WIN", x % 2 + 1, pos)
            mylcd.lcd_display_string_pos("WIN", x % 2 + 3, pos)
        x += 1
        time.sleep(0.5)
        mylcd.lcd_clear()
        for pos in pos_two:
            mylcd.lcd_display_string_pos("WIN", x % 2 + 1, pos)
            mylcd.lcd_display_string_pos("WIN", x % 2 + 3, pos)
        x += 2
        time.sleep(5)


def test_win_screen():
    mylcd.lcd_clear()
    pos_one = [1, 7, 13]
    pos_two = [4, 10, 16]
    while True:
        mylcd.lcd_display_string_pos("WIN", 1, pos_one)
        mylcd.lcd_display_string_pos("WIN", 3, pos_one)
        mylcd.lcd_display_string_pos("WIN", 2, pos_two)
        mylcd.lcd_display_string_pos("WIN", 4, pos_two)
        time.sleep(0.5)
        mylcd.lcd_clear()
        mylcd.lcd_display_string_pos("WIN", 1, pos_two)
        mylcd.lcd_display_string_pos("WIN", 3, pos_two)
        mylcd.lcd_display_string_pos("WIN", 2, pos_one)
        mylcd.lcd_display_string_pos("WIN", 4, pos_one)
        time.sleep(0.5)
        mylcd.lcd_clear()

def explode(countdown_process):
    countdown_process.terminate()
    explode_rows = rows.copy()
    explode_rows.reverse()
    while True:
        for index, row in enumerate(explode_rows):
            mylcd.lcd_clear()
            mylcd.lcd_load_custom_chars(shroom_data_list[index])
            for i in range(5):
                mylcd.lcd_display_string_pos("KABOOM", 2, 7)
                # 4- index so that it starts from the bottom and goes up, i + 15 so that the second explosion is on the right side
                mylcd.lcd_display_string_pos(chr(i), 4 - index, i)
                mylcd.lcd_display_string_pos(chr(i), 4 - index, i + 15)
            time.sleep(0.15)


def countdown(minutes: int, seconds: int):
    mylcd.lcd_clear()
    while True:
        mylcd.lcd_display_string_pos(f"{minutes:02} : {seconds:02}", 2, 7)
        mylcd.lcd_load_custom_chars(hourglass_data_list[seconds % 3])
        mylcd.lcd_display_string_pos(chr(0), 2, 5)
        mylcd.lcd_display_string_pos(chr(0), 2, 15)
        time.sleep(1)
        seconds -= 1
        if seconds < 0:
            if minutes <= 0:
                explode()
            minutes -= 1
            seconds = 59


countdown_process = multiprocessing.Process(target=countdown, args=(5, 0))

# custom chars

# shroom
shroom_top = [
    [
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00001,
        0b00011,
        0b00111,
        0b00011
    ], [
        0b00001,
        0b00111,
        0b01111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111
    ], [
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111
    ], [
        0b00000,
        0b11000,
        0b11110,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111
    ], [
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b11000,
        0b11000,
        0b11100,
        0b11000
    ]]
shroom_upper_mid = [
    [
        0b00011,
        0b00011,
        0b00001,
        0b00001,
        0b00000,
        0b00000,
        0b00000,
        0b00000
    ], [
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b01111,
        0b00111,
        0b00011
    ], [
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111
    ], [
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11110,
        0b11100,
        0b11000
    ], [
        0b11100,
        0b11100,
        0b11000,
        0b10000,
        0b00000,
        0b00000,
        0b00000,
        0b00000
    ]]
shroom_lower_mid = [
    [
        0b00001,
        0b00011,
        0b00011,
        0b00001,
        0b00000,
        0b00000,
        0b00000,
        0b00000
    ], [
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b00111,
        0b00000,
        0b00000,
        0b00001
    ], [
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b01110,
        0b11111,
        0b11111
    ], [
        0b11111,
        0b11111,
        0b11111,
        0b11111,
        0b11110,
        0b00000,
        0b00000,
        0b10000
    ], [
        0b10000,
        0b11000,
        0b11000,
        0b10000,
        0b00000,
        0b00000,
        0b00000,
        0b00000
    ]]
shroom_bot = [
    [
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00001,
        0b00111
    ], [
        0b00001,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00011,
        0b11111,
        0b11111
    ], [
        0b11111,
        0b11111,
        0b01110,
        0b01110,
        0b11111,
        0b11111,
        0b11111,
        0b11111
    ], [
        0b10000,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b11000,
        0b11111,
        0b11111
    ], [
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b11110
    ]]

shroom_data_list = [shroom_bot, shroom_lower_mid, shroom_upper_mid, shroom_top]

# hourglass

hourglass_top = [
    [
        0b11111,
        0b11111,
        0b01110,
        0b00100,
        0b01010,
        0b10001,
        0b11111,
        0b00000
    ]]
hourglass_middle = [
    [
        0b11111,
        0b10001,
        0b01110,
        0b00100,
        0b01110,
        0b10001,
        0b11111,
        0b00000
    ]]
hourglass_bot = [
    [
        0b11111,
        0b10001,
        0b01010,
        0b00100,
        0b01110,
        0b11111,
        0b11111,
        0b00000]
]

hourglass_data_list = [hourglass_bot, hourglass_middle, hourglass_top]
