# coding: utf-8

from django.shortcuts import render, get_object_or_404
from .models import Domain, Registrar, Cheapest, Price
from .models import Blog, Comment


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
    title = 'About'
    return render(request, 'about.html', {'title': title})

#Contact Page
def contact(request):
    title = 'Contact'
    return render(request, 'contact.html', {'title': title})


def blogindex(request):
    blogs = Blog.objects.all()
    return render(request, 'blogindex.html', {'blogs': blogs})

def detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'detail.html', {'blog': blog})


