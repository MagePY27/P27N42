from django.shortcuts import render
from django.http import  HttpResponse
def index(request):
    return HttpResponse("<p>hello world,hello Django</p>")
# Create your views here.
