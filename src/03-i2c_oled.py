"""
Example of I2C OLED display with SH1106 driver.

MicroPython script for initializing I2C and using an OLED
display with the SH1106 controller. The script requires
the SH1106 driver library, stored in ESP32 device.

Components:
- ESP32-based board
- OLED display with SH1106 driver
"""

from machine import I2C
from machine import Pin
from sh1106 import SH1106_I2C

# Init I2C using pins GP22 & GP21 (default I2C0 pins)
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400_000)
print(f"I2C configuration : {str(i2c)}")

# Init OLED display
oled = SH1106_I2C(i2c)

# Add some text at (x, y)
oled.text("Using OLED and", 0, 40)
oled.text("ESP32", 50, 50)


# WRITE YOUR CODE HERE


# Finally update the OLED display so the text is displayed
oled.show()
