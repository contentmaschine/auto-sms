import sys
import subprocess as sp
import os
import time

arg_list = sys.argv
del arg_list[0]
if len(arg_list) % 2 != 0:
    raise ValueError("too many/little inputs!")
pair_count = int(len(arg_list) / 2)
for i in range(pair_count):
    sp.run(["python3", os.path.join(os.getcwd(), "string_to_led.py"), str(arg_list[2 * i]), str(arg_list[2 * i + 1])])
    time.sleep(5)