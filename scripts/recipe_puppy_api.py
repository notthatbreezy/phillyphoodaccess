
# Python Wrapper for Recipe Puppy API #
# Takes an ingredient search string, turns to
# comma separated string, also will search by
# meal
import requests
import json
import pprint

pp = pprint.PrettyPrinter(indent=4)


def recipe_search(ingredient_search, meal=''):
    base_url = 'http://www.recipepuppy.com/api/?'
    ingredients = ingredient_search.replace(' ', ',')
    r = requests.get(base_url + 'i=' + ingredients + '&q=' + meal)
    result_dict = json.loads(r.text)
    return result_dict['results']

if __name__ == '__main__':
    # Example #
    search_terms = 'onions eggs'
    pp.pprint(recipe_search(search_terms))
