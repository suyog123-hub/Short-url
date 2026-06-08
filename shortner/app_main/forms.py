from django import forms
from .models import *

class Contactform(forms.ModelForm):
    class Meta:
        models = ShortURL
        fields='__all__'
