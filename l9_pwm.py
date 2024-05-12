import RPi.GPIO as gpio
import time
on = True
off = False

gpio.setmode(gpio.BOARD)
# ## PWM SETUP GUIDE
# # Set up the LED pin as a PWM with 100 duty cycles/sec
# # (that's 10 ms)
# pwmo = gpio.PWM(white, 100)
# # Start the PWM with a duty cycle of "on" 50% of the time
# pwmo.start(50)
# # Change the PWM duty cycle to on more or less of the time
# pwmo.ChangeDutyCycle(3)
# pwmo.ChangeDutyCycle(75)
# # Change the duty cycle frequency to higher or lower/sec
# # hertz rate is this number (>60 fps, we can't perceive)
# pwmo.ChangeFrequence(10)
# pwmo.ChangeFrequence(100)

# circuit 1: led circuit
# grey is ground
white = 37
grey = 39
gpio.setup(white, gpio.OUT)
pwmo = gpio.PWM(white,100)
pwmo.start(10)

# circuit 2: down button
# black is ground
red = 31
black = 30
# puts a pull-up resistor between in pin and out pin
gpio.setup(red, gpio.IN, pull_up_down=gpio.PUD_UP)

# circuit 3: up button
# purple is ground
brown = 13
purple = 14
# puts a pull-up resistor between in pin and out pin
gpio.setup(brown, gpio.IN, pull_up_down=gpio.PUD_UP)

down_button_state = 1
down_button_state_old = 1
up_button_state = 1
up_button_state_old = 1
cur_led_val = 10

try:
    while True:
        down_button_state = gpio.input(red)
        up_button_state = gpio.input(brown)
        # if button WAS depressed and is now UP:
        if down_button_state_old == 1 and down_button_state == 0:
            if cur_led_val <= 10:
                print('Reached minimum brightness. Cannot go dimmer.')
            elif cur_led_val > 10:
                cur_led_val -= 10
        if up_button_state_old == 1 and up_button_state == 0:
            if cur_led_val >= 70:
                cur_led_val = 90
                print('Reached maximum brightness. Cannot go brighter.')
            elif 30 <= cur_led_val < 70:
                cur_led_val += 20
            elif 10 <= cur_led_val < 30:
                cur_led_val += 10
        pwmo.ChangeDutyCycle(cur_led_val)
        print(f'LED is at {cur_led_val}% brightness.')
        down_button_state_old = down_button_state
        up_button_state_old = up_button_state
        time.sleep(.1)
except KeyboardInterrupt:
    gpio.cleanup()
    print('bye bye')