from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import auth

from .forms import RegistrationForm

def index(request):
	# Login part of the page
	login_form = AuthenticationForm()
	login_form.fields['username'].widget.attrs['class'] = 'center_h input_field'
	login_form.fields['username'].widget.attrs['style'] = 'margin-top: 20px;'
	login_form.fields['username'].widget.attrs['placeholder'] = 'Email'
	login_form.fields['password'].widget.attrs['class'] = 'center_h input_field'
	login_form.fields['password'].widget.attrs['style'] = 'margin-top: 5px;'
	login_form.fields['password'].widget.attrs['placeholder'] = 'Password'

	# Registration part of the page
	registration_form = RegistrationForm()
	registration_form.fields['first_name'].widget.attrs['class'] = 'center_h input_field'
	registration_form.fields['first_name'].widget.attrs['placeholder'] = 'First name'
	registration_form.fields['first_name'].widget.attrs['required'] = ''
	registration_form.fields['last_name'].widget.attrs['class'] = 'center_h input_field'
	registration_form.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
	registration_form.fields['last_name'].widget.attrs['required'] = ''
	registration_form.fields['email'].widget.attrs['class'] = 'center_h input_field'
	registration_form.fields['email'].widget.attrs['placeholder'] = 'Email'
	registration_form.fields['email'].widget.attrs['required'] = ''
	registration_form.fields['password1'].widget.attrs['class'] = 'center_h input_field'
	registration_form.fields['password1'].widget.attrs['placeholder'] = 'Password'
	registration_form.fields['password1'].widget.attrs['required'] = ''

	return render(request, 'index.html', {'login_form':login_form, 'registration_form':registration_form})

def login(request):
	if request.method == "POST":
		login_form = AuthenticationForm(request=request, data=request.POST)
		if login_form.is_valid():
			auth.login(request, login_form.get_user())
			return HttpResponseRedirect('/home')
		else:
			print(login_form.get_invalid_login_error())
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')

def registration(request):
	if request.method == "POST":
		registration_form = RegistrationForm(request.POST)
		if registration_form.is_valid():
			registration_form.fields['username'] = registration_form.cleaned_data.get('email').split("@")[0]
			registration_form.cleaned_data['username'] = registration_form.cleaned_data.get('email').split("@")[0]
			print(registration_form.cleaned_data)
			registration_form.save()
			#username = registration_form.cleaned_data.get('username')
			#raw_password = registration_form.cleaned_data.get('password1')
			#user = authenticate(username=username, password=raw_password)
			#login(request, user)
			return HttpResponseRedirect('/home')
		else:
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')

def home(request):
	if auth.get_user(request).is_authenticated:
		return HttpResponse("Hello, " + request.user.username)
	else:
		return HttpResponseRedirect('/')
