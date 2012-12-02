
# Yummly API #

import requests
from login_credentials import *
from urllib import urlencode
import pprint
import json
from operator import itemgetter
import random

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
        if len(result_dict['matches']) > 10:
            self.recipes = random.sample(result_dict['matches'], 10)
        else:
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
                recipe['ingredient_lists'] = recipe['ingredients']

    def sort_recipes(self, sort_column):
        for recipe in self.recipes:
            for nutrient in recipe['nutrition_info']:
                if nutrient['attribute'] == sort_column:
                    print "TRUE!"
                    recipe['sort_column'] = nutrient['value']
    
    def sorted_recipes_new(self):
        self.recipes_sorted = sorted(self.recipes, key=itemgetter('sort_column'))

    def get_recipe(self, recipe_id):
        yummly_key_string = "&_app_id=%s&_app_key=%s" %(yummly_app_id, yummly_app_key)
        get_url = 'http://api.yummly.com/v1/api/recipe/'+recipe_id+'?'+ self.yummly_key_string
        print get_url
        r = requests.get(get_url)
        result_dict = json.loads(r.text)
        return result_dict

    def get_daily_percents(self, dv_dictionary):
        for recipe in self.recipes:
            for nutrient in recipe['nutrition_info']:
                dv_total = dv_dictionary[nutrient['attribute']]
                try:
                    fraction = 100 * nutrient['value']/dv_total
                    nutrient['percent'] = "%.2f" % (fraction)
                except:
                    nutrient['percent'] = 'None'

    def _encode_ingredients(ingredient_string):
        """
        Takes an ingredient string, splits it into a list, and encodes it into
        an acceptable URL format
        """
        ingredient_list = [('allowedIngredient', ingredient) for ingredient in ingredient_string.split(", ")]
        return urlencode(ingredient_list)

dv_dict = {'K' : 3.5,
    'NA' : 2.4,
    'CHOLE' : 300,
    'FATRN' : 0,
    'FASAT' : 20,
    'CHOCDF' : 300,
    'FIBTG' : 25,
    'PROCNT' : 50,
    'VITC' : 0.06,
    'CA' : 1,
    'FE' : .018,
    'SUGAR' : 50,
    'ENERC_KCAL' : 2000,
    'FAT' : 65,
    'VITA_IU' : 5000}

if __name__ == '__main__':
    # print _encode_ingredients('flour, pumpkin') 
    
    # results = yummly_recipe_search('flour, pumpkin')
    # pp.pprint(results[:2])
    # print len(results)

    yummer = YummlySearch(yummly_app_id, yummly_app_key)
    # recipe = yummer.get_recipe('Pumpkin-Soup-The-Pioneer-Woman-200149')
    # pp.pprint(recipe)
    yummer.recipe_search('flour, pumpkin')
    # yummer.get_ingredients()
    # pp.pprint(yummer.recipes)