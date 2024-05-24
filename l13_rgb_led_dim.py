import RPi.GPIO as gpio
import time
on = True
off = False
gpio.setmode(gpio.BOARD)

# black = ground
black = 6
red = 37
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

# Set up PWM for pins on LED Control
pwm_red = gpio.PWM(red, 100)
pwm_green = gpio.PWM(green, 100)
pwm_blue = gpio.PWM(blue, 100)

duty_cycle_red = 0.99
duty_cycle_green = 0.99
duty_cycle_blue = 0.99

pwm_red.start(int(duty_cycle_red))
pwm_green.start(int(duty_cycle_green))
pwm_blue.start(int(duty_cycle_blue))

# Set up button states
red_button_state = 1
red_button_state_old = 1
green_button_state = 1
green_button_state_old = 1
blue_button_state = 1
blue_button_state_old = 1

try:
    while True:
        red_button_state = gpio.input(orange)
        green_button_state = gpio.input(purple)
        blue_button_state = gpio.input(white)
        if red_button_state_old == 1 and red_button_state == 0:
            duty_cycle_red = (duty_cycle_red*1.58)
            if duty_cycle_red > 99:
                duty_cycle_red = 0.99
            pwm_red.ChangeDutyCycle(int(duty_cycle_red))
        if green_button_state_old == 1 and green_button_state == 0:
            duty_cycle_green = (duty_cycle_green*1.58)
            if duty_cycle_green > 99:
                duty_cycle_green = 0.99
            pwm_green.ChangeDutyCycle(int(duty_cycle_green))
        if blue_button_state_old == 1 and blue_button_state == 0:
            duty_cycle_blue = (duty_cycle_blue*1.58)
            if duty_cycle_blue > 99:
                duty_cycle_blue = 0.99
            pwm_blue.ChangeDutyCycle(int(duty_cycle_blue))
        red_button_state_old = red_button_state
        green_button_state_old = green_button_state
        blue_button_state_old = blue_button_state
        time.sleep(.1)
except KeyboardInterrupt:
    gpio.cleanup()
    print('bye bye')
