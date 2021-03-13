from string_to_led import string_to_led
import concurrent.futures


def start_morse(words_and_pins: dict):
    n = len(words_and_pins)
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=n)
    for word in words_and_pins:
        pin = words_and_pins.get(word)
        # to handle equal keys, which don't get recognised outside of a list
        if type(pin) == list:
            for element in pin:
                executor.submit(string_to_led, word, element)
        else:
            executor.submit(string_to_led, word, pin)
