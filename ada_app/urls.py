from django.urls import path
from . import views

app_name = "ada_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("upload/", views.upload, name="upload"),
    path("browse/", views.browse, name="browse"),
	path('settings/', views.settings, name='settings'),
    path('update-settings/', views.update_settings, name='update_settings'),
]