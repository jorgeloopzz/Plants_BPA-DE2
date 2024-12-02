<h1 align="center">
    🪴 Measurement of the environment for tropical plants 🪴
</h1>

The goal of this project is to create a system that measures key environmental parameters such as temperature, humidity, light levels, soil moisture for tropical plants. This system also allows the user to visualize the data obtained.

---

- [🧑‍🧑‍🧒 Team members](#-team-members)
- [⚙️ Hardware description](#️-hardware-description)
- [🕹️ Software description](#️-software-description)
- [🖼️ Instructions and photos](#️-instructions-and-photos)
- [🛠️ References and tools](#️-references-and-tools)

&nbsp;

# 🧑‍🧑‍🧒 Team members

- Carles Tàrrega Molins
- Jorge López Viera
- Marta Tejera López

&nbsp;

# ⚙️ Hardware description

Parts used:

- ESP32
- 1 light sensor
- 2 pushbuttons
- 1 resistor
- SSD1306 OLED Display
- 1 Neopixel LED strip

![image](/assets/circuit.png)

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
- [Thonny IDE](https://thonny.org/)
- [NeoPixel](https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html)
- [Wokwi](https://wokwi.com/micropython)
- [Git](https://www.w3schools.com/git/)

&nbsp;

<div align="center">
    <a href="https://www.vut.cz/en/">
        <img src="https://img.shields.io/badge/BUT-FEEC-pass?style=for-the-badge&logo=fontawesome&logoColor=%23ffffff&labelColor=%23d12d34&color=%23173ba0
        ">
    </a>
    <a>
        <img src="https://img.shields.io/badge/ESP32-board?style=for-the-badge&logo=opensourcehardware&logoColor=%23ffffff&label=Board&labelColor=%23494d64&color=%23f5a97f
        ">
    </a>
    <a href="https://micropython.org/">
        <img src="https://img.shields.io/badge/MicroPython-board?style=for-the-badge&logo=micropython&labelColor=%232a2628&color=%23ffffff
        ">
    </a>
</div>
