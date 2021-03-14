import morse_translator
import time
import concurrent.futures
import gpiozero


pins = [5, 6, 26]

# starts n string_to_led functions, format is {pin : word}
def start_morse(pins_and_words: dict):
    n = len(pins_and_words)
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=n)
    for pin in pins_and_words:
        word = pins_and_words.get(pin)
        executor.submit(string_to_led, word, pin)


def string_to_led(message: str, pin_number: int):
    led = gpiozero.LED(pin_number)

    morse_code = morse_translator.encrypt(message)

    time_word = 2
    time_dot = 0.2
    time_dash = time_dot * 3
    time_space = 0.8
    time_between = 0.2

    while True:
        for symbol in morse_code:
            if symbol == ".":
                led.on()
                time.sleep(time_dot)
                led.off()
                time.sleep(time_between)

            if symbol == "-":
                led.on()
                time.sleep(time_dash)
                led.off()
                time.sleep(time_between)

            if symbol == " ":
                time.sleep(time_space)

        time.sleep(time_word)
