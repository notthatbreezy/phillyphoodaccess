import urllib,httplib2, mimetypes,os,sys,re,random,string
try:
	import json
except ImportError:
	import simplejson as json

####SETTINGS####
http = httplib2.Http()
url_base = 'http://www.phillysnap.com/stores/search.json/'
address = '348 N. 28th St.'
number_of_results = '5'
start_at_result = ''

def find_stores(url_base, address, number_of_results):
	url = address.replace(' ','+') + '/' + number_of_results + '/' + start_at_result
	print url
	headers = {'Content-type': 'application/x-www-form-urlencoded'}
	body = ''
	response, content = http.request(url_base+url, 'GET', headers=headers, body=urllib.urlencode(body))
	return content

print find_stores(url_base, address, number_of_results)