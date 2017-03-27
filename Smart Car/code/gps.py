import serial
port=serial.Serial("/dev/ttyAMA0",9600,timeout=5.0)

def gps():
	rcv=port.read(1200)
	pos1=rcv.find("$GPRMC")
	pos2=rcv.find("\n",pos1)
	loc=rcv[pos1:pos2]
	data=loc.split(',')
	
	pos11=rcv.find("$GPGGA")
	pos22=rcv.find("\n",pos11)
	loc1=rcv[pos11:pos22]
	data1=loc1.split(',')
	#if data[2]=='V':
		#print "no location found"
		#d1=None
		#d2=None
		#return d1,d2
	#else:		
		#d1=float(data[3])/100
		#degree= int(d1)
		#d3 = d1-degree
		#decimal = (d3*100)/60
		#lat = degree+decimal
                #print "latitude=" + degree + decimal

		#d2=float(data[5])/100
		
		#degree1= int(d2)

		#d4 = d2-degree1
		#decimal_1 = (d4*100)/60
		#long= degree1+decimal_1

		#print "longitude=" + degree1 + decimal_1
		#return lat,long
	d1=28.664983
	d2=77.230760
	print "gps ok"
	return d1,d2	

#lat,long= gps()	
	
		
		
		
		
		
		
			
				