from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import *
class Notes_form(forms.ModelForm):
    
    class Meta:
        model = Note
        fields = ('heading','text')

