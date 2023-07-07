from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

INPUT_CLASS = "w-full rounded-lg mb-3 mt-3"


class LoginForm(AuthenticationForm):
    model = User
    fields = {"username", "password"}
    username = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Enter your username', 'class': 'rounded-lg w-full mb-3 p-2'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password', 'class': 'rounded-xl w-full mb-3 p-2'}))

    # widgets = {
    #         "username": forms.TextInput(attrs={"class": INPUT_CLASS}),
    #         "password": forms.Select(attrs={'class': INPUT_CLASS}),
    #     }