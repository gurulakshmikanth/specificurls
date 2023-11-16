from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def son(request):
    return HttpResponse('<h1>nz captian</h1>')
def ravindra(request):
    return HttpResponse('<h1>battesmen</h1>')