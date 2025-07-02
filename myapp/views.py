import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Blog


def index(request):
    allblogs = Blog.objects.all()
    return render(request, "index.html", {"allblogs": allblogs})


def display(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if not blog:
        return HttpResponse("Blog not found", status=404)
    return render(request, "display.html", {"blog": blog})


def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if not blog:
        return HttpResponse("Blog not found", status=404)
    blog.delete()
    return redirect('index')


def edit(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if not blog:
        return HttpResponse("Blog not found", status=404)
    return render(request, "editForm.html", {"blog": blog})


def update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if not blog:
        return HttpResponse("Blog not found", status=404)
    blog.title = request.POST.get('title')
    blog.description = request.POST.get('description')
    blog.save()
    return redirect('index')


def createForm(request):
    return render(request, "createForm.html")


def createData(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    if not title:
        return HttpResponse("Title is required", status=400)
    blog = Blog(title=title, description=description)
    blog.save()
    return redirect('index')
