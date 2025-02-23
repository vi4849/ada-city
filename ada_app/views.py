from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.contrib import messages
from .forms import ImageFileForm
from config import API_KEY
from inference_sdk import InferenceHTTPClient
from .models import ImageFile

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key= API_KEY
)

def index(request):
    return render(request, "ada_app/home.html")

def about(request):
    return render(request, "ada_app/about.html")

def upload(request):
    if request.method == 'POST':
        form = ImageFileForm(request.POST, request.FILES)
        if form.is_valid():
            current_image = form.save()
            file_url = current_image.file.url
            
            # Send file URL to the API
            result = CLIENT.infer(file_url, model_id="accessibility-object-detection/2")
            request.session[f"predictions_{current_image.id}"] = result
            
            # Redirect to results page with the id for image that was just uploaded
            return redirect("ada_app:results", image_id=current_image.id)
    else:
        form = ImageFileForm()
    return render(request, 'ada_app/upload.html', {'form': form})
# Convert JSON-formatted prediction data into text description
def parse_predictions(prediction_data):
    predictions = prediction_data.get("predictions", [])
    
    if not predictions:
        return "No objects detected in the image."
    
    description = []
    
    for pred in predictions:
        obj_class = pred.get("class", "unknown object")
        confidence = round(pred.get("confidence", 0) * 100, 2)
        description.append(f"Detected a {obj_class} with {confidence}% confidence.")
    
    return " ".join(description)

def results(request, image_id):
    image_instance = get_object_or_404(ImageFile, pk=image_id)
    
    # Retrieve prediction results from session
    prediction_data = request.session.get(f"predictions_{image_id}", {})
    
    # Convert JSON predictions into a readable description
    description = parse_predictions(prediction_data)

    return render(
        request,
        "ada_app/results.html",
        {
            "image": image_instance,
            "description": description,
            "prediction_data": prediction_data,
        },
    )

def browse(request):
    return render(request, "ada_app/browse.html")

def settings(request):
    return render(request, 'ada_app/settings.html')

def ada(request):
    return render(request, 'ada_app/ada.html')

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