from django import forms
from .models import ImageFile
from django.core.exceptions import ValidationError

class ImageFileForm(forms.ModelForm):
    class Meta:
        model = ImageFile
        fields = ['file']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        
    def clean(self):
        cleaned_data = super().clean()
        file = cleaned_data.get('file')
        
        if file:
            if file.size > 5 * 1024 * 1024:
                self.add_error('file', "Image file too large ( > 5MB )")
            if not file.content_type.startswith('image'):
                self.add_error('file', "File type is not an image")
        else:
            self.add_error('file', "No file selected")
        return cleaned_data
    
