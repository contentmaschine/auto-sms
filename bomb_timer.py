import time
import sys


def countdown(minutes: int, seconds: int):
    while True:
        sys.stdout.write("\r{minutes} : {seconds}".format(minutes=minutes, seconds=seconds))
        sys.stdout.flush()
        time.sleep(1)
        seconds -= 1
        if seconds <= 0:
            if minutes <= 0:
                sys.stdout.write("\r{minutes} : {seconds}".format(minutes=minutes, seconds=seconds))
                time.sleep(1)
                return "boom"
            minutes -= 1
            seconds = 59
