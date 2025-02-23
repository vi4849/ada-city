from django.db import models
import json

# Create your models here.

# File model
class ImageFile(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    predictions = models.JSONField(default=dict, blank=True)
