
# Yummly API #

import requests
from login_credentials import *
from urllib import urlencode
import pprint
import json

pp = pprint.PrettyPrinter(indent=4)

def yummly_recipe_search(ingredient_string):
    yummly_key_string = "&_app_id=%s&_app_key=%s" %(yummly_app_id, yummly_app_key)
    # ingredient_list = _encode_ingredients(ingredient_string)
    payload = {'_app_id' : yummly_app_id, '_app_key' : yummly_app_key, 'q' : ingredient_string, 'maxResults' : 72}
    get_url = 'http://api.yummly.com/v1/api/recipes?allowedAttribute=course%5Ecourse-Desserts'
    r = requests.get(get_url, params=payload)
    print r.url
    result_dict = json.loads(r.text)
    return result_dict

def _encode_ingredients(ingredient_string):
    """
    Takes an ingredient string, splits it into a list, and encodes it into
    an acceptable URL format
    """
    ingredient_list = [('allowedIngredient', ingredient) for ingredient in ingredient_string.split(", ")]
    return urlencode(ingredient_list)

if __name__ == '__main__':
    # print _encode_ingredients('flour, pumpkin') 
    results = yummly_recipe_search('flour, pumpkin')
    pp.pprint(results)
    print len(results['matches'])