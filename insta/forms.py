from dataclasses import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# class CommentForm (forms.ModelForm):
#   class Meta:
#     model=Comment
#     exclude=['image','user']
class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image','caption']
        exclude = ['user']