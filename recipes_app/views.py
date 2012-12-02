# Create your views here.
from models import *
import urllib,httplib2, mimetypes,os,sys,re,random,string
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from subprocess import call
import string
from yummly_api import *
from login_credentials import *
from django.shortcuts import redirect


def recipe_search(request):
    return render_to_response('recipe_home.html', context_instance=RequestContext(request))

def recipe_results(request):
    if request.POST:
        ingredients = request.POST['i']
        # ingredients = ingredients.translate(string.maketrans("",""), string.punctuation)
        yummer = YummlySearch(yummly_app_id, yummly_app_key)
        yummer.recipe_search(ingredients)
        yummer.get_ingredients()
        try:
            yummer.get_daily_percents(dv_dict)
        except:
            return redirect('/search_again/')
        # yummer.sort_recipes('ENERC_KCAL')
        # yummer.sorted_recipes_new()

        if len(yummer.recipes) == 0:
            return render_to_response('recipe_results.html', {"noResults":"No recipes with those ingredients..."})
        else:
            return render_to_response('recipe_results.html', {"recipes":yummer.recipes}, context_instance=RequestContext(request))
    else:
        return redirect('/')
