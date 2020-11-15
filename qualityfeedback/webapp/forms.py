from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

class LoginForm(forms.Form):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'center_h input_field', 'style':'margin-top: 20px;'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'center_h input_field', 'style':'margin-top: 5px;'}))
