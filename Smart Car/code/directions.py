import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDC_r378-T6lf9pdi076O3QdUiX5dxFzRo')
now = datetime.now()
directions_result = gmaps.directions("Kashmere gate Metro Station, New Delhi",
                                     "Indira Gandhi Delhi Technical University for Women, Kashmere Gate, New Delhi",
                                     mode="driving",
                                     departure_time=now)
#use origin instead of input of current location 
print (directions_result)
