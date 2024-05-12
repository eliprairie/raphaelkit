import RPi.GPIO as gpio
import time
on = True
off = False

# circuit 1: determines whether button is pressed
# brown is ground
black = 40
brown = 39

# circuit 2: determines whether LED is on or off
# grey is ground
white = 38
grey = 34

gpio.setmode(gpio.BOARD)
# puts a pull-up resistor between in pin and out pin
gpio.setup(black, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(white, gpio.OUT)

led_on = False
button_state = 1
button_state_old = 1

try:
    while True:
        button_state = gpio.input(black)
        print(button_state)
        # if button WAS depressed and is now UP:
        if button_state_old == 1 and button_state == 0:
            # if led_on was true, make it false, vice versa.
            led_on = not led_on
            gpio.output(white, led_on)
        button_state_old = button_state
        time.sleep(.1)
except KeyboardInterrupt:
    print('bye bye')
    gpio.cleanup()