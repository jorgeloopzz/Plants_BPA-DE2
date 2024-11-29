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
        return presses
