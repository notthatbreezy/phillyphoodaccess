
# Test FatSecret API #
from fatsecret import Fatsecret
import pprint
consumer_key = '28372c2342794218abbac88b8434fccf'
consumer_secret = '1eff849e38354f858dfb525384447a0b'

fs=Fatsecret(consumer_key,consumer_secret)
pp = pprint.PrettyPrinter(indent=4)

result=fs.foods_search("Toast")
print pp.pprint(result)