from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import *
class Article_form(forms.ModelForm):
    title = forms.Field(widget=forms.TextInput(attrs={'required':True}))
    class Meta:
        model = Articles
        fields = ('title','image','video','category','tags','facebook','instagram','quora','medium','twitter','other','description','content')


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=150)


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', )


class CommentForm(forms.ModelForm):
	class Meta:
		model = my_comment
		fields = ('name', 'email', 'body')

class Contribute(forms.ModelForm):
    class Meta:
        model = Aptitude
        fields = ('question','A','B','C','D','E','topic','category','company','correct','difficulty','explanation')

class ListingForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ('description','heading')

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('title','category','tags')

class AnwserForm(forms.ModelForm):
    class Meta:
        model = Anwsers
        fields = ('explanation',)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'