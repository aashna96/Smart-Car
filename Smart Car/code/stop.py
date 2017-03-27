import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

def stop():
	while True:
		GPIO.output(18,False)
		GPIO.output(20,False)
		GPIO.output(21,False)
		GPIO.output(22,False)
        