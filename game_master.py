from string_to_led import string_to_led
import concurrent.futures


# the pins are 5, 6, 26 from left to right
def start_morse(pins_and_words: dict):
    n = len(pins_and_words)
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=n)
    for pin in pins_and_words:
        word = pins_and_words.get(pin)
        executor.submit(string_to_led, word, pin)
