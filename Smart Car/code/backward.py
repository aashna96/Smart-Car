import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

while True:
	GPIO.output(17,True)
	GPIO.output(18,False)
	GPIO.output(23,True)
	GPIO.output(24,False)
	
	
