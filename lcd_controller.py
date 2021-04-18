import RPi_I2C_driver
import time

mylcd = RPi_I2C_driver.lcd()

shroom_data_top = [
	[
		0b00000,
		0b00000,
		0b00000,
		0b00000,
		0b00001,
		0b00011,
		0b00111,
		0b00011
	], [
		0b00001,
		0b00111,
		0b01111,
		0b11111,
		0b11111,
		0b11111,
		0b11111,
		0b11111
	], [
		0b11111,
		0b11111,
		0b11111,
		0b11111,
		0b11111,
		0b11111,
		0b11111,
		0b11111
	], [
		0b00000,
		0b11000,
		0b11110,
		0b11111,
		0b11111,
		0b11111,
		0b11111,
		0b11111
	], [
		0b00000,
		0b00000,
		0b00000,
		0b00000,
		0b11000,
		0b11000,
		0b11100,
		0b11000
	]]
shroom_data_upper_mid = [
	[
		0b00011,
		0b00011,
		0b00001,
		0b00001,
		0b00000,
		0b00000,
		0b00000,
		0b00000
	], [
		0b11111,
		0b11111,
		0b11111,
		0b11111,
		0b11111,
		0b01111,
		0b00111,
		0b00011
	], [
		0b11111,
		0b11111,
		0b11111,
		0b11111,
		0b11111,
		0b11111,
		0b11111,
		0b11111
	], [
		0b11111,
		0b11111,
		0b11111,
		0b11111,
		0b11111,
		0b11110,
		0b11100,
		0b11000
	], [
		0b11100,
		0b11100,
		0b11000,
		0b10000,
		0b00000,
		0b00000,
		0b00000,
		0b00000
	]]
shroom_data_lower_mid = [
	[
		0b00001,
		0b00011,
		0b00011,
		0b00001,
		0b00000,
		0b00000,
		0b00000,
		0b00000
	], [
		0b11111,
		0b11111,
		0b11111,
		0b11111,
		0b00111,
		0b00000,
		0b00000,
		0b00001
	], [
		0b11111,
		0b11111,
		0b11111,
		0b11111,
		0b11111,
		0b01110,
		0b11111,
		0b11111
	], [
		0b11111,
		0b11111,
		0b11111,
		0b11111,
		0b11110,
		0b00000,
		0b00000,
		0b10000
	], [
		0b10000,
		0b11000,
		0b11000,
		0b10000,
		0b00000,
		0b00000,
		0b00000,
		0b00000
	]]
shroom_data_bot = [
	[
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
	], [
		0b11111,
		0b11111,
		0b01110,
		0b01110,
		0b11111,
		0b11111,
		0b11111,
		0b11111
	], [
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
shroom_data_list = [shroom_data_bot, shroom_data_lower_mid, shroom_data_upper_mid, shroom_data_top]
shroom_data_list.reverse()
rows = [0x80, 0xC0, 0x94, 0xD4]
#rows.reverse()

def start_screen():
	mylcd.lcd_display_string_pos("KEEP RASPI", 2, 5)
	mylcd.lcd_display_string_pos("TALKING", 3, 6)


def explode():
	try:
		while True:
			for index, row in enumerate(rows):
				mylcd.lcd_load_custom_chars(shroom_data_list[index])
				mylcd.lcd_write(row)
				for x in range(4):
					for i in range(5):
						mylcd.lcd_write_char(i)
				time.sleep(0.15)
				mylcd.lcd_clear()
	except:
		mylcd.lcd_clear()
