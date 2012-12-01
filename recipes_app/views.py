# Create your views here.
from models import *
import urllib,httplib2, mimetypes,os,sys,re,random,string
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from subprocess import call
import string
from recipe_puppy_api import *

def recipe_search(request):
    return render_to_response('recipe_home.html', context_instance=RequestContext(request))

def recipe_results(request):
    ingredients = request.POST['i']
    # ingredients = ingredients.translate(string.maketrans("",""), string.punctuation)
    recipes = recipe_puppy_search(ingredients)
    return render_to_response('recipe_results.html', {"recipes":recipes}, context_instance=RequestContext(request))