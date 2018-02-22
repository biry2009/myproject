from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def blogindex(request):
    return HttpResponse("Hello, This is the blog index page")