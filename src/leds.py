from machine import Pin
from neopixel import NeoPixel
from time import sleep

pixels = NeoPixel(Pin(15), 16)

def off():
  off = (0, 0, 0) 

  for i in range(16):
    pixels[i] = off
  pixels.write()
  sleep(0.1)
  

def blue():
  azul = (0, 102, 255) 
  for i in range(16):
    pixels[i] = azul
  pixels.write()
  sleep(0.1)

def red():
  rojo = (255, 0, 0) 
  for i in range(16):
    pixels[i] = rojo
  pixels.write()
  sleep(0.1)

def uv():
  purple = (153, 51, 255) 
  for i in range(16):
    pixels[i] = purple
  pixels.write()
  sleep(0.1)

def white():
  white = (255, 255, 255) 
  for i in range(16):
    pixels[i] = white
  pixels.write()
  sleep(0.1)

def yellow():
  yellow = (255, 255, 0) 
  for i in range(16):
    pixels[i] = yellow
  pixels.write()
  sleep(0.1)

def green():
  green = (0, 204, 0) 
  for i in range(16):
    pixels[i] = green
  pixels.write()
  sleep(0.1)
