from geopy import geocoders 

print 'Encoding Origin'

def encode_origin(origin_address):
	g = geocoders.Google()
	place, (lat, lng) = g.geocode(origin_address)
	return [lat,lng]
	
print encode_origin('755 N. 26th St. Philadelphia PA 19130')