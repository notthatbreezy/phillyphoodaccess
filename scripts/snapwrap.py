import requests, urllib
try:
	import json
except ImportError:
	import simplejson as json

#I like the name, SnapWrap!
class SnapWrap(object):

	'''examples:
	test = SnapWrap()
	print test.json_r
	print test.json_r['market']['fulltext']

	test1 = SnapWrap(address="1500 N Broad St",max_results=10)
	print test1.json_r
	print test1.json_r['market']['fulltext']

	test2 = SnapWrap(max_results=10,start_result=5)

	'''

	#Default values, we may decide later to not do a default for address.
	def __init__(self,address="1500 Market St",max_results=None,start_result=None):
		self.base_url = "http://www.phillysnap.com/stores/search.json/"
		self.address = address
		self.max_results = max_results
		self.start_result = start_result
		self.json_r = self._request() #json_r short for "json response"

	def _request(self):
		self.address_enc = urllib.quote_plus(self.address)

		#this crummy nested if determines if you have a max_results and a start_result.
		#The API requires a max_results if you want a start_result. So you can't pick and choose.
		if self.max_results is None:
				self.request_url = self.base_url + self.address_enc + "/"
		else:
			if self.start_result is not None:
				self.request_url = self.base_url + self.address_enc + "/" + str(self.max_results) + "/" + str(self.start_result)
			else:
				self.request_url = self.base_url + self.address_enc + "/" + str(self.max_results)

		# r is an actual Python Requests response object, see http://docs.python-requests.org/en/latest/api/
		#for other attributes you could use
		r = requests.get(self.request_url)
		return r.json