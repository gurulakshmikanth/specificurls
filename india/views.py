from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def virat(request):
    return HttpResponse('<h1>50 th centure in od</h1>')
def rohith(request):
    return HttpResponse('<h1> indian team captian')