
# Yummly API #

import requests
from login_credentials import *
from urllib import urlencode
import pprint
import json

pp = pprint.PrettyPrinter(indent=4)

class YummlySearch():
    """
    Manages API calls to Yummly for Recipe Searches and Recipe Information
    """
    def __init__(self, app_id, app_key):
        self.yummly_key_string = "&_app_id=%s&_app_key=%s" %(app_id, app_key)
        self.app_id = app_id
        self.app_key = app_key

    def recipe_search(self, ingredient_string):
        # ingredient_list = _encode_ingredients(ingredient_string)
        payload = {'_app_id' : yummly_app_id, '_app_key' : yummly_app_key, 'q' : ingredient_string, 'maxResults' : 5}
        get_url = 'http://api.yummly.com/v1/api/recipes?'
        r = requests.get(get_url, params=payload)
        print get_url
        result_dict = json.loads(r.text)
        self.recipes = result_dict['matches']

    def get_ingredients(self):
        def _get_recipe(recipe_id):
            yummly_key_string = "&_app_id=%s&_app_key=%s" %(yummly_app_id, yummly_app_key)
            get_url = 'http://api.yummly.com/v1/api/recipe/'+recipe_id+'?'+self.yummly_key_string
            print get_url
            r = requests.get(get_url)
            result_dict = json.loads(r.text)
            return result_dict
        for recipe in self.recipes:
            try:
                recipe_result = _get_recipe(recipe['id'])
                recipe['nutrition_info'] = recipe_result['nutritionEstimates']
                recipe['ingredient_lists'] = recipe_result['ingredientLines']
            except:
                recipe['ingredient_lists'] = recipe_result['ingredients']

    def get_recipe(self, recipe_id):
        yummly_key_string = "&_app_id=%s&_app_key=%s" %(yummly_app_id, yummly_app_key)
        get_url = 'http://api.yummly.com/v1/api/recipe/'+recipe_id+'?'+self.yummly_key_string
        print get_url
        r = requests.get(get_url)
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
    
    # results = yummly_recipe_search('flour, pumpkin')
    # pp.pprint(results[:2])
    # print len(results)

    yummer = YummlySearch(yummly_app_id, yummly_app_key)
    # recipe = yummer.get_recipe('Pumpkin-Soup-The-Pioneer-Woman-200149')
    # pp.pprint(recipe)
    yummer.recipe_search('flour, pumpkin')
    yummer.get_ingredients()
    pp.pprint(yummer.recipes)