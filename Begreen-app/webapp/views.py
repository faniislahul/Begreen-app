from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
from webapp.models import *
from django.views.generic import *


# Create your views here.
def index(request):
    return render(request,'webapp/index.html')

def categories(request):
    return render(request,'webapp/categories.html')

def products(request):
    return render(request,'webapp/products.html')
