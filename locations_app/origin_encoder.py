from geopy import geocoders
import json

print 'Encoding Origin'

def encode_origin(origin_address):
	origin_address += '&components=administrative_level:'
	g = geocoders.Google()
	place, (lat, lng) = g.geocode(origin_address)
	return [lat,lng]

def reverse_encode_origin(latlon):
	coordinates = str(latlon[0]) + ',' + str(latlon[1]) + '&components=administrative_area:Philadelphia'
	g = geocoders.Google()
	print g.reverse(coordinates)

latlon = encode_origin('755 N. 26th St.')
print latlon	
