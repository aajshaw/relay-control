import RPi.GPIO as GPIO
import sys

if len(sys.argv) != 3:
    print('Usage: python3 relay-control.py GPIO-pin-number [on|off]')
    exit()

pin = int(sys.argv[1])
set_to = sys.argv[2].lower()

if pin < 0 or pin > 27:
    print('GPIO pin must be between 0 and 27')
    exit()

if set_to not in ('on', 'off'):
    print('GPIO pin can be set to either on or off')
    exit()

# GPIO.cleanup() is not called because the pin is to be left as HIGH or LOW when the program exits
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
if set_to == 'on':
    GPIO.output(pin, GPIO.HIGH)
else:
    GPIO.output(pin, GPIO.LOW)
