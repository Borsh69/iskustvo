from django import forms
from .models import *


class LoginForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ['text'] 