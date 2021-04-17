import RPi_I2C_driver

mylcd = RPi_I2C_driver.lcd()

bomb_icon_data = [
    [
    0b00000,
    0b00001,
    0b00011,
    0b00011,
    0b00011,
    0b00011,
    0b00001,
    0b00000
    ],
    #bot mid
    [
    0b00100,
    0b11111,
    0b11111,
    0b11111,
    0b11111,
    0b11111,
    0b11111,
    0b11111
    ],
    [
    0b00000,
    0b10000,
    0b11000,
    0b11000,
    0b11000,
    0b11000,
    0b10000,
    0b00000
    ],
    # mid left
    [
    0b00001,
    0b00001,
    0b00101,
    0b10000,
    0b00000,
    0b00001,
    0b00000,
    0b00000],

    # mid mid
    [
    0b11111,
    0b11111,
    0b11111,
    0b01110,
    0b00100,
    0b00010,
    0b00100,
    0b00100
    ],
    # mid right
    [
    0b10000,
    0b10101,
    0b10000,
    0b00000,
    0b01000,
    0b00000,
    0b00000,
    0b00000
    ]
    # ,
    # #top mid
    # [
    # 0b00000,
    # 0b00000,
    # 0b00000,
    # 0b00000,
    # 0b00000,
    # 0b01110,
    # 0b11111,
    # 0b11111
    # ]
]

mylcd.lcd_load_custom_chars(bomb_icon_data)

mylcd.lcd_write(0x80)
mylcd.lcd_write_char(3)
mylcd.lcd_write_char(4)
mylcd.lcd_write_char(5)

mylcd.lcd_write(0xC0)

mylcd.lcd_write_char(0)
mylcd.lcd_write_char(1)
mylcd.lcd_write_char(2)

mylcd.lcd_write(0x94)

mylcd.lcd_write_char(0)
mylcd.lcd_write_char(1)
mylcd.lcd_write_char(2)

mylcd.lcd_write(0xD4)

mylcd.lcd_write_char(0)
mylcd.lcd_write_char(1)
mylcd.lcd_write_char(2)