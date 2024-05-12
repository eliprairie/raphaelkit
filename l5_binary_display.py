import RPi.GPIO as gpio
import time
on = True
off = False
one = 21
two = 19
four = 5
eight = 27
sixteen = 17
leds = [one, two, four, eight, sixteen]
gpio.setmode(gpio.BCM)
for led in leds:
    gpio.setup(led,gpio.OUT)

#############
# Blink Test:
#############
# blink = input('How many times do you want the LED to blink?: ')
# blink = int(blink)
# timer = 0

# while timer < blink:
#     for led in leds:
#         gpio.output(led, on)
#         time.sleep(1)
#         gpio.output(led, off)
#         time.sleep(1)
#         timer += 1

i = 0
while i <= 31:
    print(i)
    # Convert i into a binary number
    bini = format(i,'05b')
    print(f'in binary, {i} is {bini}')
    digits = list(int(bini))
    gpio.output(one, digits[4])
    gpio.output(two, digits[3])
    gpio.output(four, digits[2])
    gpio.output(eight, digits[1])
    gpio.output(sixteen, digits[0])
    time.sleep(2)
    i += 1

gpio.cleanup()