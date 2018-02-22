# coding: utf-8

from django.shortcuts import render
from .models import Domain, Registrar, Cheapest, Price


from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def reviews(request):
    registrars = Registrar.objects.all()
    return render(request, 'reviews.html', {'registrars': registrars})

# Registrar Review Page
def review(request, name):
    registrar = Registrar.objects.filter(keyword=name)
    if registrar:
        return render(request, 'review.html')
    else:
        return render(request, '404.html')


def domain(request, name):
    return render(request, 'tld_base.html')


#About Page
def about(request):
    return render(request, 'about.html')

#Contact Page
def contact(request):
    return render(request, 'contact.html')


