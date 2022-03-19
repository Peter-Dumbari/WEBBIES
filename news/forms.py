from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from news.models import *
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length = 254, widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(max_length = 254, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(max_length = 254, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model  = User
        fields = ("username","first_name", "last_name", "email")


class LoginForm(AuthenticationForm):
     username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class':'form-control'}))
     password = forms.CharField(max_length = 254, widget=forms.PasswordInput(attrs={'class':'form-control'}))

class AddNewsForm(forms.ModelForm):
    topic =  forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class':'form-control'}))
    article =  forms.CharField(max_length=254, widget=forms.Textarea(attrs={'class':'form-control', 'col': '5'}))
    class Meta:
        model = BlogNews
        fields = ("topic", "article")


