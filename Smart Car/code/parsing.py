import googlemaps
import json
import urllib3
from urllib3.exceptions import InsecurePlatformWarning
import forward
#lat=28.664983
#long=77.230760
#destination="IGDTUW, Kashmere Gate,New Delhi"
urllib3.disable_warnings(InsecurePlatformWarning)
#logging.captureWarnings(True)
def parsing(lat, long,destination):
	urllib3.disable_warnings(InsecurePlatformWarning)
	gmaps = googlemaps.Client(key="AIzaSyDC_r378-T6lf9pdi076O3QdUiX5dxFzRo")
	geocode_result=gmaps.directions((lat,long),destination,mode="walking")
	urllib3.disable_warnings()
	length=len(geocode_result)
	result=geocode_result[0]
	for i in range(2,(length-1)):
		result=result+geocode_result[i] 
	result_1=result['legs']
	
	length=len(result_1)
	result_2=result_1[0]
	for i in range(2,(length-1)):
		result_2=result_2+result_1[i] 
	result_3=result_2['steps']
	
	length=len(result_3)
	result_4=result_3[0]
	for i in range(2,(length-1)):
		result_4=result_4+result_3[i] 
	result_5=result_4['html_instructions']
	
	string=result_5[0]
	for i in range(1,4):
		string=string+result_5[i]
	string=string.encode('utf8')
	
	string1=result_5.encode('utf8')
	flag=0
	if string=="Head":
   		for i in range (5,len(string1)-1):
      			if string1[i]==">":
      				direction=string1[i+1]	
      				while string1[i+2]!="<":
					direction=direction+string1[i+2]
					i=i+1
				flag=1

			elif flag==1:
				break
	 		else:
	 			i=i+1		
	else:
	 	print "No Direction"
	
	print direction
	length=len(direction)
	if direction =="north":
	 	print "forward"
	elif direction =="south":
	 	print "backward"
	elif direction =="east":
	 	print "right"
	elif direction =="west":
	 	print "left"
	elif direction =="northeast":
		forward.forward()
	elif direction =="northwest":
		print "forward"
	elif direction =="southeast":
		print "backward"
	elif direction =="southwest":
		print "backward"
	 	
#parsing(lat,long,destination)	 	  					

































































































































































































































































































































































































































































