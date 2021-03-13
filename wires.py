import gpiozero
import time


cuttable_wires_pin = 27
do_not_cut_wires_pin = 17

cuttable_wires_still_connected = gpiozero.Button(cuttable_wires_pin).is_pressed
do_not_cut_wires_still_connected = gpiozero.Button(do_not_cut_wires_pin).is_pressed

while True:
    if not cuttable_wires_still_connected:
        print("success")
        pass
    if not do_not_cut_wires_still_connected:
        print("STRIKE")
    time.sleep(0.1)
