import morse_translator
import RPi.GPIO as gpio
import time
import concurrent.futures


# starts n string_to_led functions, format is {pin : word}
def start_morse(pins_and_words: dict):
    n = len(pins_and_words)
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=n)
    for pin in pins_and_words:
        word = pins_and_words.get(pin)
        executor.submit(string_to_led, word, pin)


def string_to_led(message: str, pin_number: int):
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)
    gpio.setup(pin_number, gpio.OUT)

    morse_code = morse_translator.encrypt(message)

    time_word = 2
    time_dot = 0.2
    time_dash = time_dot * 3
    time_space = 0.8
    time_between = 0.2

    while True:
        for symbol in morse_code:
            if symbol == ".":
                gpio.output(pin_number, gpio.HIGH)
                time.sleep(time_dot)
                gpio.output(pin_number, gpio.LOW)
                time.sleep(time_between)

            if symbol == "-":
                gpio.output(pin_number, gpio.HIGH)
                time.sleep(time_dash)
                gpio.output(pin_number, gpio.LOW)
                time.sleep(time_between)

            if symbol == " ":
                time.sleep(time_space)

        time.sleep(time_word)
