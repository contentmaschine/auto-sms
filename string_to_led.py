import morse_translator as mt
import RPi.GPIO as gpio
import time
import sys
import subprocess as sp
import os
import concurrent.futures as cf


def string_to_led(message: str, pin_number: int):
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)
    gpio.setup(pin_number, gpio.OUT)

    morse_code = mt.encrypt(message)

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


try:
    executor = cf.ThreadPoolExecutor(max_workers=3)
    a = executor.submit(string_to_led, "SOS", 5)
    b = executor.submit(string_to_led, "ATA", 6)

finally:
    gpio.cleanup()
