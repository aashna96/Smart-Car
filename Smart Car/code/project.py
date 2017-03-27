import RPi.GPIO as GPIO
import time
import serial
GPIO.setmode(GPIO.BCM)
port=serial.Serial("/dev/ttyAMA0",9600,timeout=10.0)


t=23
e=24

ir1=17
ir2=27

led_pin=16

print "send something from android"

print "distance"

GPIO.setup(t,GPIO.OUT)
GPIO.setup(e,GPIO.IN)
GPIO.setup(ir1,GPIO.IN)
GPIO.setup(ir2,GPIO.IN)


GPIO.setup(18,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

safe_distance=8

while True:
	port.flushInput()
	port.flushOutput()
	
	rcv=port.read(50)
	
	if rcv:
		print "message" +rcv
		GPIO.output(led_pin,GPIO.HIGH)
	else:
		print "try again"
	
	GPIO.output(t,False)
	print "waiting for sensor to settle"
	time.sleep(2)
	GPIO.output(t,True)
	time.sleep(0.00001)
	GPIO.output(t,False)
	while GPIO.input(e)==0:
		pulse_start=time.time()
	while GPIO.input(e)==1:
		pulse_end=time.time()
	pulse_duration=pulse_end-pulse_start
	distance=pulse_duration*17150
	
	if distance<safe_distance
		if GPIO.input(ir1) and GPIO.input(ir2):
			#stop
			GPIO.output(18,False)
			GPIO.output(20,False)
			GPIO.output(21,False)
			GPIO.output(22,False)
		elif GPIO.input(ir1):
			#right
			GPIO.output(18,True)
			GPIO.output(20,True)
			GPIO.output(21,False)
			GPIO.output(22,True)
		elif GPIO.input(ir2):
			#left
			GPIO.output(18,False)
			GPIO.output(20,True)
			GPIO.output(21,False)
			GPIO.output(22,False)
		else:
			#left
			GPIO.output(18,False)
			GPIO.output(20,True)
			GPIO.output(21,False)
			GPIO.output(22,False)
	else:
		#forward
		GPIO.output(18,False)
		GPIO.output(20,True)
		GPIO.output(21,False)
		GPIO.output(22,True)
	
	time.sleep(1)					
		 		


 