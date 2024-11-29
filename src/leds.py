from machine import Pin
from neopixel import NeoPixel
from time import sleep

n=20
pixels = NeoPixel(Pin(25), n)

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

def red():
  rojo = (255, 0, 0) 
  for i in range(n):
    pixels[i] = rojo
  pixels.write()
  sleep(0.1)

def uv():
  purple = (153, 51, 255) 
  for i in range(n):
    pixels[i] = purple
  pixels.write()
  sleep(0.1)

def white():
  white = (255, 255, 255) 
  for i in range(n):
    pixels[i] = white
  pixels.write()
  sleep(0.1)

def yellow():
  yellow = (255, 255, 0) 
  for i in range(n):
    pixels[i] = yellow
  pixels.write()
  sleep(0.1)

def green():
  green = (0, 204, 0) 
  for i in range(n):
    pixels[i] = green
  pixels.write()
  sleep(0.1)
