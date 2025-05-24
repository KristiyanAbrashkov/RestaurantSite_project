from django.forms import ModelForm
from .models import Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        exclude = ['author']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']