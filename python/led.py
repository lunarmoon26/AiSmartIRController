import RPi.GPIO as GPIO
import time

pin_out = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_out, GPIO.OUT)

n = 0
while n < 1000:
    GPIO.output(pin_out, True)
    time.sleep(1)
    GPIO.output(pin_out, False)
    time.sleep(1)
    n += 1