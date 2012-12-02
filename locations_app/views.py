from models import *
import urllib,httplib2, mimetypes,os,sys,re,random,string
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from subprocess import call
from snapwrap import *
from origin_encoder import *

# Create your views here.

def home(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def direction_results(request):
    start_address = request.GET['d']
    phillysnap_results = SnapWrap(address=start_address)
    map_dictionary = phillysnap_results.json_r
    map_dictionary['origin'] = encode_origin(start_address)
    return render_to_response('directions.html', {'map_dictionary': map_dictionary}) #context_instance=RequestContext(request))
