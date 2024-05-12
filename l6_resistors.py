import RPi.GPIO as gpio
import time
on = True
off = False

# circuit 1: determines whether button is pressed
red = 1
black = 39
# brown is ground
brown = 40

# circuit 2: determines whether LED is on or off
white = 38
# grey is ground
grey = 34

gpio.setmode(gpio.BOARD)
gpio.setup(brown, gpio.IN)
gpio.setup(white, gpio.OUT)

try:
    while True:
        readVal = gpio.input(brown)
        # if the switch is pressed (interrupt), turn LED on
        if readVal == 0:
            gpio.output(white, on)
        # if switch is not pressed (circuit open), keep LED off
        elif readVal == 1:
            gpio.output(white, off)
except KeyboardInterrupt:
    print('bye bye')
    gpio.cleanup()
