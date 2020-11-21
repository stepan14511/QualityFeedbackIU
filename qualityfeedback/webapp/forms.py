from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class RegistrationForm(UserCreationForm):
    first_name = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'})
    last_name = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'})
    email = forms.EmailField()

    password1 = forms.CharField()
    password2 = None

    class Meta(UserCreationForm.Meta):
        model = User
        # I've tried both of these 'fields' declaration, result is the same
        fields = ('first_name', 'last_name', 'email', 'password1')
        #fields = UserCreationForm.Meta.fields
