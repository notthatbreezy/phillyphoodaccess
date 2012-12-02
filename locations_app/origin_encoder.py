from geopy import geocoders
import json

def encode_origin(origin_address):
	origin_address += 'Philadelphia,PA'
	g = geocoders.Google()
	place, (lat, lng) = g.geocode(origin_address)
	return [lat,lng]