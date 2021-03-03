import morse_translator as mt
import RPi.GPIO as gpio
import time


def string_to_led(message: str, pin_number: int):
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)
    gpio.setup(pin_number, gpio.OUT)

    morse_code = mt.encrypt(message)

    while True:
        for symbol in morse_code:
            if symbol == ".":
                gpio.output(pin_number, gpio.HIGH)
                time.sleep(0.2)
                gpio.output(pin_number, gpio.LOW)
                time.sleep(0.2)

            if symbol == "-":
                gpio.output(pin_number, gpio.HIGH)
                time.sleep(0.6)
                gpio.output(pin_number, gpio.LOW)
                time.sleep(0.2)

            if symbol == " ":
                time.sleep(1)

