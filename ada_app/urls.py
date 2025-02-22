from django.urls import path
from . import views

app_name = "ada_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("upload/", views.upload, name="upload"),
    path("browse/", views.browse, name="browse"),
]