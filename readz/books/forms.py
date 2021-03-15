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
  class Meta:
    model = posts
<<<<<<< HEAD
    fields = ["Comment"]
    labels = {'Comment': "Comment"}


class bookInputForm(forms.ModelForm):
    class Meta:
        model = user_collection
        fields = ('title', 'image')
=======
    fields = ["Comment","Name"]
    labels = {'Comment': "Comment",'Name':"Name"}
>>>>>>> 45266788720e949fc56c763242d611f71c27f84c