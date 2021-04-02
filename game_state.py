from gpiozero import LED
from signal import pause
import concurrent.futures


strike_counter = 0
wires_done = False
simon_says_done = False
sms_done = False


def strike(strike_pins: tuple=(23, 24, 25)):
    global strike_counter
    active_pin = strike_pins[strike_counter]

    executor = concurrent.futures.ThreadPoolExecutor()
    executor.submit(strike_led_on, active_pin)

    strike_counter += 1
    if strike_counter > 2:
        # explode
        raise AttributeError("you exploded")


def strike_led_on(active_pin: int):
    strike_led = LED(active_pin)
    strike_led.on()
    pause()

def success_led_on(active_pin):
    success_led = LED(active_pin)
    success_led.on()
    pause()

def success(success_pin: int):
    executor = concurrent.futures.ThreadPoolExecutor()
    executor.submit(success_led_on(success_pin))
