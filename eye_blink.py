# 2 LEDs where one blinks occasionally
# for a Jack O Lantern's eyes

import RPi.GPIO as GPIO
import time

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the
# pin positions
GPIO.setmode(GPIO.BCM)
left_eye = 18
right_eye = 23
BLINK_INTERVAL = 20  # seconds
OPEN_INTERVAL = 15   # seconds

GPIO.setup(left_eye, GPIO.OUT)
GPIO.setup(right_eye, GPIO.OUT)
        
try:
    # Now just blink both
    while True:
        # Turn on both eyes
        GPIO.output(left_eye, True)
        GPIO.output(right_eye, True)
        time.sleep(OPEN_INTERVAL)
        GPIO.output(left_eye, False)
        GPIO.output(right_eye, False)
        time.sleep(BLINK_INTERVAL)
finally:
    print("Cleaning up")
    GPIO.cleanup()
