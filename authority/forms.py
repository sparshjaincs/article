from django import forms

from .models import *

class Mock_Form(forms.ModelForm):
    class Meta:
        model = Mock
        fields = ('title','company','pattern')

class Series_Form(forms.ModelForm):
    class Meta:
        model = Test_Series
        fields = ("title",)