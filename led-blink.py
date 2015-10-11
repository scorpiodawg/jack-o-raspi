import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)


GPIO.output(7, True)

for count in range(10):
    time.sleep(2)
    GPIO.output(7, False)
    time.sleep(1)
    GPIO.output(7, True)

GPIO.output(7, False)
