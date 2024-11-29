from machine import Pin, PWM, ADC, I2C
import sh1106
import dht12
import time
import leds
import random
import Button

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
sensor = dht12.DHT12(i2c)
photosensor = ADC(Pin(34))
button1 = Button.Button(27)
button2 = Button.Button(26)
oled_width = 128
oled_height = 64
oled = sh1106.SH1106_I2C(i2c)
show_initial_message=0
ledoff=0

try:
    while True:
            oled.fill(0)#Como un clear
            sensor.measure()
            temp = sensor.temperature()
            humidity = sensor.humidity()
            light = photosensor.read()

            oled.text('Temp: {:.1f}C'.format(temp), 0, 0)
            oled.text('Humidity: {:.1f}%'.format(humidity), 0, 20)
            oled.text('Light: {:.1f}lux'.format(light), 0, 40)
            oled.show()
            time.sleep(1)
            oled.fill(0)

            if 15<temp<20 and 50<humidity<70 and 800<light<2000:
                leds.blue()
                oled.text('Turn on Blue Light', 0, 20)
                oled.text('Promotes initial growth', 0, 30)
                oled.text('growth', 0, 40)
                oled.show()
                time.sleep(1.5)
                oled.fill(0)

            elif temp>25 and 40<humidity<60 and light>2000:
                leds.red()
                oled.text('Turn on Red Light', 0, 20)
                oled.text('Promotes flower', 0, 30)
                oled.text('and fruit', 0, 40)
                oled.show()
                time.sleep(1.5)
                oled.fill(0)

            elif 20<temp<25 and 40<humidity<96 and 1000<light<2000:
                    oled.text('No extra light', 0, 20)
                    oled.show()
                    leds.off()
                    time.sleep(3)
                    oled.fill(0)

            elif 15<temp<25 and humidity<50 and light>2000:
                leds.uv()
                oled.text('Turn on UV Light', 0, 20)
                oled.text('Antioxidants Production', 0, 30)
                oled.text('Stress Resistance', 0, 40)
                oled.show()
                time.sleep(1.5)
                oled.fill(0)

            elif 15<temp<30 and 70<humidity<96 and light>1000:
                leds.white()
                oled.text('Turn on White Light', 0, 20)
                oled.text('Balanced spectrum ', 0, 30)
                oled.text('for continuous growth', 0, 40)
                oled.show()
                time.sleep(10)
                oled.fill(0)


            else:
                npressbutton1 = button1.get_presses()
                npressbutton2 = button2.get_presses()
                if show_initial_message==0 or ledoff==1:
                    oled.text('Click the button', 0, 20)
                    oled.text('to find out', 0, 30)
                    oled.text('which plant its:', 0, 40)
                    oled.show()
                    time.sleep(3)  # Espera para leer el botón
                    oled.fill(0)
                    show_initial_message = 1

                if npressbutton1 == 0:
                    time.sleep(3)
                    oled.fill(0)
                elif npressbutton1 == 1:
                    while npressbutton2 == 0:
                        oled.fill(0)
                        leds.yellow()
                        oled.text('Small Plant', 0, 0)
                        oled.text('Turn on Yellow', 0, 10)
                        oled.text('Promotes initial', 0, 20)
                        oled.text('& control growth', 0, 30)
                        oled.show()
                        time.sleep(3)
                        npressbutton2 = button2.get_presses()
                        npressbutton1=0
                    leds.off()
                    ledoff=1
                    oled.fill(0)
                elif npressbutton1 == 2:
                    while npressbutton2 == 0:
                        oled.fill(0)
                        leds.green()
                        oled.text('Medium Plant', 0, 0)
                        oled.text('Turn on Green', 0, 10)
                        oled.text('Supports lower', 0, 20)
                        oled.text('plant parts', 0, 30)
                        oled.show()
                        time.sleep(3)
                        npressbutton2 = button2.get_presses()
                        npressbutton1=0
                    leds.off()
                    ledoff=1
                    oled.fill(0)
                elif npressbutton1 >= 3:
                    while npressbutton2 == 0:
                        oled.fill(0)
                        leds.red()
                        oled.text('Big/Mature Plant', 0, 0)
                        oled.text('Turn on Red', 0, 10)
                        oled.text('Promotes flower', 0, 20)
                        oled.text('Energy efficiency', 0, 30)
                        oled.show()
                        time.sleep(1.5)
                        npressbutton2 = button2.get_presses()
                        npressbutton1=0
                    leds.off()
                    ledoff = 1

            oled.fill(0)
            leds.off()
            oled.show()
            time.sleep(0.5)

finally:
    leds.off()
    oled.fill(0)
    oled.show()
