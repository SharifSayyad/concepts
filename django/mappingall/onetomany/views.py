from django.shortcuts import render
from django.http import HttpResponse
print('inside views.py')
# Create your views here.

def welcome(request):
    s = 'Welcome functions from onetomany'
    return HttpResponse(s)
