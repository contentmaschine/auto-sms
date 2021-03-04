from string_to_led import string_to_led
import concurrent.futures


def start_morse(words_and_pins: dict):
    n = len(words_and_pins)
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=n)
    for word in words_and_pins:
        pin = words_and_pins.get(word)
        executor.submit(string_to_led, word, pin)
