# 2 LEDs where one blinks occasionally
# for a Jack O Lantern's eyes

import RPi.GPIO as GPIO
import time

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the
# pin positions
GPIO.setmode(GPIO.BCM)
left_eye = 18
right_eye = 23
BLINK_INTERVAL = 10  # seconds

GPIO.setup(left_eye, GPIO.OUT)
GPIO.setup(right_eye, GPIO.OUT)
        
try:
    # Turn on both eyes
    GPIO.output(left_eye, True)
    GPIO.output(right_eye, True)
    # Now just blink the left eye every 10 seconds
    while True:
        time.sleep(BLINK_INTERVAL)
        GPIO.output(left_eye, False)
        time.sleep(0.25)
        GPIO.output(left_eye, True)
finally:
    print("Cleaning up")
    GPIO.cleanup()
