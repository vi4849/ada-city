from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.core.files.storage import default_storage
from config import API_KEY
from inference_sdk import InferenceHTTPClient

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key= API_KEY
)

def index(request):
    return render(request, "ada_app/home.html")

def about(request):
    return render(request, "ada_app/about.html")

def upload(request):
    if request.method == "POST":
        # Handle file upload
        file = request.FILES["imageFile"]
        file_name = default_storage.save(file.name, file)
        file_url = default_storage.path(file_name)

        print(f"File saved at: {file_url}")

        result = CLIENT.infer(file_url, model_id="accessibility-object-detection/2")
        return render(request, "ada_app/upload.html", {"predictions": result})

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