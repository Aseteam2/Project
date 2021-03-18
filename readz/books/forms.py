from django import forms
from .models import posts
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.auth.password_validation import NumericPasswordValidator
from django.contrib.auth.password_validation import validate_password

from .models import user_collection


class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(), validators=[validate_password] )
    confirm_password = forms.CharField(widget = forms.PasswordInput(), validators=[validate_password] )
    #email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    class Meta():
        model =User
        fields =('username', 'email', 'password', 'confirm_password')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class postform(forms.ModelForm):
    Comment=forms.CharField(max_length=500,widget=forms.Textarea(attrs={'class' : 'form-control'}))
    Name=forms.CharField(max_length=100,widget=forms.HiddenInput(attrs={'class' : 'form-control'}))
    class Meta:
        model = posts
        fields = ('Comment', 'Name')
    


class bookInputForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    class Meta:
        model = user_collection
        fields = ('title', 'image')

 

