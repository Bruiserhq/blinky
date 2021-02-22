import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and s$
while True: # Run forever

 GPIO.output(8, GPIO.HIGH) # Turn on
 sleep(1) # Sleep (stay on) for  (x) seconds
 GPIO.output(8, GPIO.LOW) # Turn off
 sleep(.5) # Sleep for (x) seconds
