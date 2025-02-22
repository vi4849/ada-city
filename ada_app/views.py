from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.dispatch import receiver

def index(request):
    return render(request, "ada_app/home.html")

def about(request):
    return render(request, "ada_app/about.html")

def upload(request):
    return render(request, "ada_app/upload.html")

def browse(request):
    return render(request, "ada_app/browse.html")