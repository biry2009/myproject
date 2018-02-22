from django.shortcuts import render

from .models import Blog, Comment



# Create your views here.


def blogindex(request):
    blogs = Blog.objects.all()
    return render(request, 'blogindex.html', {'blogs': blogs})