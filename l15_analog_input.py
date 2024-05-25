import RPi.GPIO as gpio
import ADC0834 as adc #/usr/lib/ADC0834.py
import time

# board setup
on = True
off = False
gpio.setmode(gpio.BCM)

# setup for red LED
led = 21
gpio.setup(led,gpio.OUT)
pwm_red = gpio.PWM(led, 1000)
duty_cycle_red = 0.99
pwm_red.start(int(duty_cycle_red))

# setup for ADC module
adc.setup()

# setup for analog dial
led_intensity = 0

try:
    while True:
        led_intensity = adc.getResult(0)
        pwm_red.ChangeDutyCycle(int(led_intensity)*0.39)
        time.sleep(.1)
except KeyboardInterrupt:
    gpio.cleanup()
    print('\nbye bye')