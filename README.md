<h1 align="center">
    🪴 Measurement of the environment for tropical plants 🪴
</h1>

The goal of this project is to create a system that measures key environmental parameters such as temperature, humidity, light levels, soil moisture for tropical plants. This system also allows the user to visualize the data obtained.

- [⚙️ Hardware description](#️-hardware-description)
- [🕹️ Software description](#️-software-description)
- [🖼️ Instructions and photos](#️-instructions-and-photos)
- [🛠️ References and tools](#️-references-and-tools)

&nbsp;

# ⚙️ Hardware description

Parts used:

- [ESP32](/assets/esp32.png)
- 1 light sensor
- DHT12 sensor
- 2 pushbuttons
- 1 resistor
- SSD1306 OLED Display
- 1 Neopixel LED strip

![image](/assets/circuit.png)

<details>
  <summary>More details</summary>
    - For NeoPixel, 1 pin for voltage, other for ground, and the last connected to any digital input. <br>
    - 2 of the 4 pushbuttons pins must be disconnected, the other 2 can be connected to any digital input. <br>
    - Since OLED display requires I2C commmunications we need to connect the correspond pins to SDA and SCL, pins 21 and 22.
</details>

&nbsp;

# 🕹️ Software description

### ✅ Test files

```
src/
├── 01-i2c_scan.py
├── 02-i2c_rtc.py
├── 02-i2c_sensor.py
├── 02-i2c_sensor_bme280.py
├── 03-i2c_oled.py
├── 04-i2c_sensor_oled.py
├── sh1106_org.py
└── sh1106.py
```

### 🗃️ Classes

```
src/
├── bme280.py
├── Button.py
└── dht12.py
```

> 📝 **Note:** the `Button` class was made by ourselves, apart for controlling pushbuttons, to know and control when they are pressed.
>
```python
# src/Button.py
from machine import Pin
import time

class Button:
    def __init__(self, pin_number):
        self.button = Pin(pin_number, Pin.IN, Pin.PULL_UP)
        self.npressbutton = 0
        self.last_press_time = 0
        self.button.irq(trigger=Pin.IRQ_FALLING, handler=self.button_is_pressed)

    """Check if button is pressed"""
    def button_is_pressed(self, pin):
        current_time = time.ticks_ms()
        if time.ticks_diff(current_time, self.last_press_time) > 200:  # Antirrebote de 200ms
            self.last_press_time = current_time
            self.npressbutton += 1

    """Count every time button is pressed"""
    def get_presses(self):
        presses = self.npressbutton
        time.sleep(3)
        self.npressbutton = 0  # Reinicia después de leer
        return presses.
```

### 🎨 Colours

In order to manage lights we've made functions to change each pixel color through a **_for_** loop.

```python
# src/leds.py
...

def off():
  off = (0, 0, 0)
  for i in range(n):
    pixels[i] = off
  pixels.write()
  sleep(0.1)

def blue():
  azul = (0, 102, 255)
  for i in range(n):
    pixels[i] = azul
  pixels.write()
  sleep(0.1)

...
```

&nbsp;

# 🖼️ Instructions and photos

|           **_Flowchart 1_**           |           **_Flowchart 2_**           |
| :-----------------------------------: | :-----------------------------------: |
| ![flowchart1](/assets/flowchart1.png) | ![flowchart2](/assets/flowchart2.png) |

&nbsp;

|          **_Result 1_**          |          **_Result 2_**          |
| :------------------------------: | :------------------------------: |
| ![result1](/assets/result1.jpeg) | ![result2](/assets/result2.jpeg) |

&nbsp;

# 🛠️ References and tools

- [Course repository](https://github.com/tomas-fryza/esp-micropython)
- [Markdown guide](https://www.markdownguide.org/)
- [Plants lights](https://www.sansiled.com/blogs/learn/full-guide-how-to-choose-the-right-led-grow-light-for-indoor-plants?srsltid=AfmBOoqe4BZMuldTM41Fa41uPQ0RgtTld7ecW41ph5GGAbkUcQqhSEnm)
- [Thonny IDE](https://thonny.org/)
- [NeoPixel](https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html)
- [Wokwi](https://wokwi.com/micropython)
- [Git](https://www.w3schools.com/git/)

&nbsp;

<div align="center">
    <a href="https://www.vut.cz/en/">
        <img src="https://img.shields.io/badge/BUT-FEEC-pass?style=for-the-badge&logo=fontawesome&logoColor=%23ffffff&labelColor=%23d12d34&color=%23173ba0">
    </a>
    <a href="https://en.wikipedia.org/wiki/ESP32">
        <img src="https://img.shields.io/badge/ESP32-board?style=for-the-badge&logo=opensourcehardware&logoColor=%23ffffff&label=Board&labelColor=%23494d64&color=%23f5a97f">
    </a>
    <a href="https://micropython.org/">
        <img src="https://img.shields.io/badge/MicroPython-board?style=for-the-badge&logo=micropython&labelColor=%232a2628&color=%23ffffff">
    </a>
</div>
