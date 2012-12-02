from geopy import geocoders
import json

def encode_origin(origin_address):
	origin_address += 'Philadelphia,PA'
	g = geocoders.Google()
	place, (lat, lng) = g.geocode(origin_address)#, exactly_one=False)
	print lat,lng,place
	return "{\"origin\":{\"latitude\":" + str(lat) + ",\"longitude\":"+str(lng)+"}}"
	
print encode_origin('755 N. 26th St')