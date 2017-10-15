from django.contrib.auth.models import User
from django import forms

class UserForm(forms.Form):
    password =forms.CharField(widget= forms.passwordInput)
    
    class Meta:
        model= User
        fields= ['username','email','password']
