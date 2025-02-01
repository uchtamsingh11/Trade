from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class SignupForm(forms.ModelForm):
    username = forms.CharField(max_length=150, label="User ID")
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    name = forms.CharField(max_length=100)
    mobile_no = forms.CharField(max_length=15)
    referral = forms.CharField(max_length=20, required=False)

    class Meta:
        model = UserProfile
        fields = ["username", "email", "name", "mobile_no", "referral", "password"]


class LoginForm(forms.Form):
    username = forms.CharField(label="User ID")
    password = forms.CharField(widget=forms.PasswordInput)
