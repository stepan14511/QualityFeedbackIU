from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class RegistrationForm(UserCreationForm):
	first_name = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
	last_name = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
	email = forms.EmailField()

	password1 = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

	def clean(self):
		p1 = self.cleaned_data["password1"]
		p2 = self.cleaned_data["password2"]
		if p1 and p2 and p1 != p2:
			raise forms.ValidationError( self.error_messages['password_mismatch'],
										 code='password_mismatch' )
		return self.cleaned_data

	def save(self):
		role = 'student'
		username = self.cleaned_data.get('email').split("@")[0]
		email = self.cleaned_data.get('email')
		first_name = self.cleaned_data.get('first_name')
		last_name = self.cleaned_data.get('last_name')
		password = self.cleaned_data.get('password2')
		return User.objects.create_user(email=email, username=username, password=password, first_name=first_name, last_name=last_name, role=role)
