from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.auth.password_validation import NumericPasswordValidator

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model =User
        fields =('username', 'email', 'password')
