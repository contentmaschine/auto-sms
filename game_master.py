from string_to_led import string_to_led
import concurrent.futures


#the pins are 5, 6, 26 from left to right
def start_morse(words_and_pins: dict):
    n = 3
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=n)
    for word in words_and_pins:
        pin = words_and_pins.get(word)
        # to handle equal keys, which don't get recognised outside of a list
        if isinstance(pin, list):
            for element in pin:
                executor.submit(string_to_led, word, element)
        else:
            executor.submit(string_to_led, word, pin)
