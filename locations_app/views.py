from models import *
import urllib,httplib2, mimetypes,os,sys,re,random,string
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse
from subprocess import call

# Create your views here.

def home(request):
    return render_to_response('index.html')
