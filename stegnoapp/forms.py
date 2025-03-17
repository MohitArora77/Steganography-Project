from django import forms
from .models import StegoImage

class StegoImageForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea, required=False, label="Message (for encoding)")
    
    class Meta:
        model = StegoImage
        fields = ['image', 'message']
