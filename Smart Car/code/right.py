import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

while True:
	GPIO.output(17,True)
	GPIO.output(18,True)
	GPIO.output(23,False)
	GPIO.output(24,True)
	
	
