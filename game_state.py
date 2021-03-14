import gpiozero

counter = 0


def strike(strike_pins=(23, 24, 25)):
    global counter
    active_pin = strike_pins[counter]
    strike_led = gpiozero.LED(active_pin)
    strike_led.on()
    counter += 1
    if counter >= 3:
        # explode
        pass


def success(success_pin=16):
    success_led = gpiozero.LED(success_pin)
    success_led.on()
    # do win
    pass
