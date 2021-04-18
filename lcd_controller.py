import RPi_I2C_driver
import time

mylcd = RPi_I2C_driver.lcd()

shroom_data_one = [[
	0b00000,
	0b00000,
	0b00000,
	0b00000,
	0b00001,
	0b00011,
	0b00111,
	0b00111
],[
	0b00001,
	0b00111,
	0b01111,
	0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b11111
],[
	0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b11111
],[
	0b00000,
	0b11000,
	0b11110,
	0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b11111
],[
	0b00000,
	0b00000,
	0b00000,
	0b00000,
	0b11000,
	0b11000,
	0b11100,
	0b11110
]]

shroom_data_two = [[
	0b00011,
	0b00011,
	0b00001,
	0b00001,
	0b00000,
	0b00000,
	0b00000,
	0b00000
],[
	0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b01111,
	0b00111,
	0b11111
],[
	0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b11111
],[
	0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b11110,
	0b11100,
	0b11111
],[
	0b11100,
	0b11100,
	0b11000,
	0b10000,
	0b00000,
	0b00000,
	0b00000,
	0b00000
]]

shroom_data_three = [[
	0b00011,
	0b00011,
	0b00011,
	0b00001,
	0b00000,
	0b00000,
	0b00000,
	0b00000
],[
	0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b00111,
	0b00000,
	0b00000,
	0b00001
],[
	0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b01110,
	0b11111,
	0b11111
],[
	0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b11110,
	0b00000,
	0b00000,
	0b10000
],[
	0b11000,
	0b11000,
	0b11000,
	0b10000,
	0b00000,
	0b00000,
	0b00000,
	0b00000
]]
shroom_data_four = [[
	0b00000,
	0b00000,
	0b00000,
	0b00000,
	0b00000,
	0b00000,
	0b00001,
	0b00111
], [
	0b00001,
	0b00000,
	0b00000,
	0b00000,
	0b00000,
	0b00011,
	0b11111,
	0b11111
],[
	0b11111,
	0b11111,
	0b01110,
	0b01110,
	0b11111,
	0b11111,
	0b11111,
	0b11111
],[
	0b10000,
	0b00000,
	0b00000,
	0b00000,
	0b00000,
	0b11000,
	0b11111,
	0b11111
], [
	0b00000,
	0b00000,
	0b00000,
	0b00000,
	0b00000,
	0b00000,
	0b00000,
	0b11110
]]

shroom_data_list = [shroom_data_one, shroom_data_two, shroom_data_three, shroom_data_four]
shroom_data_list = shroom_data_list.reverse()

rows = [0xD4, 0x94, 0xC0, 0x80]

try:
	while True:
		for index, row in enumerate(rows):
			# minus index because we want to start at the bottom i.e. four
			mylcd.lcd_load_custom_chars(shroom_data_list[index])
			mylcd.lcd_write(row)
			for i in range (5):
				mylcd.lcd_write_char(i)
			time.sleep(0.5)
			mylcd.lcd_clear()
except:
	mylcd.lcd_clear()
