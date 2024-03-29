from django import forms
from .models import posts
from .models import Comment
from django.db import models
from .models import user_collection

from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.auth.password_validation import NumericPasswordValidator
from django.contrib.auth.password_validation import validate_password


# this file manages all the forms used in project. It is used for defining the forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(), validators=[validate_password] )
    confirm_password = forms.CharField(widget = forms.PasswordInput(), validators=[validate_password] )
   
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta():
        model =User
        fields =('username','first_name','last_name','email', 'password', 'confirm_password')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class bookInputForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    class Meta:
        model = user_collection
        fields = ('title','image')


class postform(forms.ModelForm):
    Title=forms.CharField(max_length=500,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    Comment=forms.CharField(max_length=500,widget=forms.Textarea(attrs={'class' : 'form-control'}))
    Name=forms.CharField(max_length=100,widget=forms.HiddenInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = posts
        fields = ('Comment', 'Name', 'Title')
    




class commentform(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    body = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class' : 'form-control'}))
    class Meta:
        model = Comment
        fields = ('name','body')

        

