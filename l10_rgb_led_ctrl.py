import RPi.GPIO as gpio
import time
on = True
off = False
gpio.setmode(gpio.BOARD)

# black = ground
black = 6
red = 15
green = 13
blue = 11

gpio.setup(red, gpio.OUT)
gpio.setup(green, gpio.OUT)
gpio.setup(blue, gpio.OUT)

