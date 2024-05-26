import RPi.GPIO as gpio
import ADC0834 as adc #/usr/lib/ADC0834.py
import time

# board setup
on = True
off = False
gpio.setmode(gpio.BCM)

# setup for RGB LED
red = 25
green = 21
blue = 23
# Sets up RGB wires and sets all LED control to OFF
gpio.setup(red, gpio.OUT)
gpio.setup(green, gpio.OUT)
gpio.setup(blue, gpio.OUT)

# Set up PWM for pins on LED Control
pwm_red = gpio.PWM(red, 1000)
pwm_green = gpio.PWM(green, 1000)
pwm_blue = gpio.PWM(blue, 1000)

duty_cycle_red = 0.99
duty_cycle_green = 0.99
duty_cycle_blue = 0.99

pwm_red.start(int(duty_cycle_red))
pwm_green.start(int(duty_cycle_green))
pwm_blue.start(int(duty_cycle_blue))

red_intensity = 0
green_intensity = 0
blue_intensity = 0

# setup for ADC module
adc.setup()

try:
    while True:
        red_intensity = adc.getResult(0)
        print(f'red is at {red_intensity}')
        pwm_red.ChangeDutyCycle(int(red_intensity)*0.39)
        green_intensity = adc.getResult(1)
        print(f'green is at {green_intensity}')
        pwm_green.ChangeDutyCycle(int(green_intensity)*0.39)
        blue_intensity = adc.getResult(2)
        print(f'blue is at {blue_intensity}')
        pwm_blue.ChangeDutyCycle(int(blue_intensity)*0.39)
        time.sleep(.2)
except KeyboardInterrupt:
    gpio.cleanup()
    print('\nbye bye')