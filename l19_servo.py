import RPi.GPIO as gpio
import time
on = True
off = False
gpio.setmode(gpio.BOARD)

# brown = ground
brown = 6
red = 1
orange = 12

# set up for orange (control) as pwm with (1/0.02 or 50hz DC)
gpio.setup(orange, gpio.OUT)
pwm_orange = gpio.PWM(orange, 50)
pwm_orange.start(0)

try:
    while True:
        pwm_percent = float(input('angle % = '))
        pwm_orange.ChangeDutyCycle(pwm_percent)
        time.sleep(.1)
except KeyboardInterrupt:
    gpio.cleanup()
    print('\nbye bye')
