import RPi.GPIO as gpio
import time
on = True
off = False
gpio.setmode(gpio.BOARD)

# black = ground
black = 6
red = 29
green = 13
blue = 11

# circuit 1: red switch
orange = 40
# puts a pull-up resistor between in pin and out pin
gpio.setup(orange, gpio.IN, pull_up_down=gpio.PUD_UP)

# circuit 2: green switch
purple = 33
# puts a pull-up resistor between in pin and out pin
gpio.setup(purple, gpio.IN, pull_up_down=gpio.PUD_UP)

# circuit 3: blue switch
white = 22
# puts a pull-up resistor between in pin and out pin
gpio.setup(white, gpio.IN, pull_up_down=gpio.PUD_UP)

# Sets up RGB wires and sets all LED control to OFF
gpio.setup(red, gpio.OUT)
gpio.setup(green, gpio.OUT)
gpio.setup(blue, gpio.OUT)

red_button_state = 1
red_button_state_old = 1
red_led_on = False
red_led_intensity = 0
green_button_state = 1
green_button_state_old = 1
green_led_on = False
green_led_intensity = 0
blue_button_state = 1
blue_button_state_old = 1
blue_led_on = False
blue_led_intensity = 0

try:
    while True:
        red_button_state = gpio.input(orange)
        green_button_state = gpio.input(purple)
        blue_button_state = gpio.input(white)
        if red_button_state_old == 1 and red_button_state == 0:
            red_led_on = not red_led_on
            gpio.output(red, red_led_on)
        if green_button_state_old == 1 and green_button_state == 0:
            green_led_on = not green_led_on
            gpio.output(green, green_led_on)
        if blue_button_state_old == 1 and blue_button_state == 0:
            blue_led_on = not blue_led_on
            gpio.output(blue, blue_led_on)
        red_button_state_old = red_button_state
        green_button_state_old = green_button_state
        blue_button_state_old = blue_button_state
        time.sleep(.1)
except KeyboardInterrupt:
    gpio.cleanup()
    print('bye bye')
