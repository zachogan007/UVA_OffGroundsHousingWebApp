from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import User


class UserForm(UserCreationForm):
    name = forms.CharField(max_length=200, required=True,
                           widget=forms.TextInput(attrs={'placeholder: Your name here'}))
    year = forms.CharField(max_length=200, required=True,
                           widget=forms.TextInput(attrs={'placeholder: Your year here'}))

    class Meta:
        model = User
        fields = ('name', 'year')

