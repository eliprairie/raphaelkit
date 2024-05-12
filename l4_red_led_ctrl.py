import RPi.GPIO as gpio
import time
led = 11
on = True
off = False
gpio.setmode(gpio.BOARD)
gpio.setup(led,gpio.OUT)

blink = input('How many times do you want the LED to blink?: ')
blink = int(blink)
timer = 0

while timer < blink:
    gpio.output(led, on)
    time.sleep(1)
    gpio.output(led, off)
    time.sleep(1)
    timer += 1

gpio.cleanup()