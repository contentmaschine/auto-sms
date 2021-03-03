from string_to_led import string_to_led
import concurrent.futures
import RPi.GPIO as gpio

try:
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)
    executor.submit(string_to_led, "Y", 6)
    executor.submit(string_to_led, "A", 5)
    executor.submit(string_to_led, "Y", 26)
except KeyboardInterrupt:
    gpio.cleanup()