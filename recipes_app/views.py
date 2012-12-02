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

def recipe_search(request):
    return render_to_response('recipe_home.html', context_instance=RequestContext(request))

def recipe_results(request):
    ingredients = request.POST['i']
    # ingredients = ingredients.translate(string.maketrans("",""), string.punctuation)
    yummer = YummlySearch(yummly_app_id, yummly_app_key)
    yummer.recipe_search(ingredients)
    yummer.get_ingredients()
    return render_to_response('recipe_results.html', {"recipes":yummer.recipes}, context_instance=RequestContext(request))