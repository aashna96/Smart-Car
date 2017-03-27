import parsing
import gps
import RPi.GPIO as GPIO
import time
import stop
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#GPIO.setup(26,GPIO.IN)

pin=26

a=0
while True:
	#input_state=GPIO.input(pin)
	input_state=True
	time.sleep(2)
	if input_state==True:
		global a
		a=1
		global destination
		destination=raw_input("Enter the destination : ")
		break
while (a):
	if a%2 !=0:
		lat,long=gps.gps()
		if lat!=None and long!=None:
			parsing.parsing(lat,long,destination)
	time.sleep(0.5)
	#if input_state==True:
	#	a=a+1
	#	stop.stop() 
	#input_state=GPIO.input(pin)
	#time.sleep(1)