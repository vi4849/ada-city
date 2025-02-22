from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.contrib import messages
from .forms import ImageFileForm


def index(request):
    return render(request, "ada_app/home.html")

def about(request):
    return render(request, "ada_app/about.html")

def upload(request):
    if request.method == 'POST':
        form = ImageFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ImageFileForm()

    return render(request, 'ada_app/upload.html', {'form': form})

def browse(request):
    return render(request, "ada_app/browse.html")


