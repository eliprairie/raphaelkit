import RPi.GPIO as gpio
import ADC0834 as adc #/usr/lib/ADC0834.py
import time

# board setup
on = True
off = False
gpio.setmode(gpio.BCM)

# setup for pull-up resistor for click
click = 21
gpio.setup(click, gpio.IN, pull_up_down=gpio.PUD_UP)
# Set up button states
click_button_state = 1
click_button_state_old = 1

# setup for ADC module
adc.setup()

try:
    while True:
        x_val = adc.getResult(0)
        time.sleep(.1)
        y_val = adc.getResult(1)
        click_button_state = gpio.input(click)
        print(f'x_val={x_val} | y_val={y_val} | click_state={click_button_state}')
        time.sleep(.2)
except KeyboardInterrupt:
    gpio.cleanup()
    print('\nbye bye')