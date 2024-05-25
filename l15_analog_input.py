import RPi.GPIO as gpio
import ADC0834 as adc #/usr/lib/ADC0834.py
import time
on = True
off = False
gpio.setmode(gpio.BCM)

adc.setup()

try:
    while True:
        output_value = adc.getResult(0)
        print(output_value)
        time.sleep(.2)
except KeyboardInterrupt:
    gpio.cleanup()
    print('\nbye bye')