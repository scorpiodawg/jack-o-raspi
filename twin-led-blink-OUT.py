import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
#GPIO.setup(7, GPIO.OUT)
#GPIO.output(7, True)

print "Setting 18 and 23 to output"
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

print "Turning them ON..."
GPIO.output(18, True)
GPIO.output(23, True)

for count in range(10):
    print "Once more..."
    time.sleep(0.5)
    # GPIO.output(7, False)
    GPIO.output(18, False)
    GPIO.output(23, True)
    time.sleep(0.5)
    # GPIO.output(7, True)
    GPIO.output(18, True)
    GPIO.output(23, False)

# GPIO.output(7, False)
print "Turning pins OFF"
GPIO.output(18, False)
GPIO.output(23, False)

print "Done!"
