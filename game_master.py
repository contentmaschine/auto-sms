from string_to_led import string_to_led
import concurrent.futures

executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)
executor.submit(string_to_led, "Y", 5)
executor.submit(string_to_led, "A", 6)
executor.submit(string_to_led, "Y", 26)