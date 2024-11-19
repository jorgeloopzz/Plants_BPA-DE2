# Class for controlling Leds

import machine, neopixel

np = neopixel.NeoPixel(machine.Pin(1), 1)

np[0] = (255, 255, 26)

np.write()