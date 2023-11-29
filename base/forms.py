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
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-regist'}),
            'tag': forms.TextInput(attrs={'class': 'form-regist'}),
            'avatar': forms.FileInput(attrs={'class': 'form-regist'}),
            'password': forms.PasswordInput(attrs={'class': 'form-regist', type: 'password'}),
            'login': forms.TextInput(attrs={'class': 'form-regist'})

        }

class AddArtWork(forms.Form):
    face = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-regist'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-regist'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-regist'}))
    uncompressed_img = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-regist'}), required=False)
    object3d = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-regist'}), required=False)
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-regist', 'placeholder':'example1, example2, example3'}), required=False)
