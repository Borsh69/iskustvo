from django import forms
from .models import *


class LoginForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ['text'] 

class RegistForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['name','tag', 'avatar', 'login', 'password'] 