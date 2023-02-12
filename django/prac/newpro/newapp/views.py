from django.shortcuts import render
from django.urls import URLPattern

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('HEllO WORLD')