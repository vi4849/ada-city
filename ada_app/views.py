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

def settings(request):
    return render(request, 'ada_app/settings.html')

def update_settings(request):
    """Handle form submission for updating user preferences."""
    if request.method == "POST":
        # Get values from the form
        color_scheme = request.POST.get("color_scheme", "default")
        font_size = request.POST.get("font_size", "medium")

        # Save preferences in the session
        request.session["color_scheme"] = color_scheme
        request.session["font_size"] = font_size

        # Redirect back to settings page with updated preferences
        return redirect("ada_app:settings")