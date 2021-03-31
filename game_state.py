from gpiozero import LED


strike_counter = 0


def strike(strike_pins=(23, 24, 25)):
    global strike_counter
    active_pin = strike_pins[strike_counter]
    strike_led = LED(active_pin)
    strike_led.on()
    strike_counter += 1
    if strike_counter > 2:
        # explode
        raise AttributeError("you exploded")
    return strike_counter


def success(success_pin=16):
    success_led = LED(success_pin)
    success_led.on()
    # do win
    pass
