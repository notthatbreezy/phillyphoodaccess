import requests, json, urllib

class SnapConsumer(object):

	def __init__(self,address="1500 Market St",max_results=None,start_result=None):
		self.base_url = "http://www.phillysnap.com/stores/search.json/"
		self.address = address
		self.max_results = max_results
		self.start_result = start_result

	def __call__(self):
		self.address_enc = urllib.quote_plus(self.address)
		if self.max_results is None:
				self.request_url = self.base_url + self.address_enc + "/"
		else:
			if self.start_result is not None:
				self.request_url = self.base_url + self.address_enc + "/" + self.max_results + "/" + self.start_result
			else:
				self.request_url = self.base_url + self.address_enc + "/" + self.max_results
		self.snapresponse = self.get(self.request_url)
		return self.snapresponse

	def get(url):
		r = requests.get(url)
		return json.loads(r.content)
		
if __name__=='__main__':
    from pprint import pprint
    test = SnapConsumer()
    pprint(test)