from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def index(request):
	login_form = AuthenticationForm()
	login_form.fields['username'].widget.attrs['class'] = 'center_h input_field'
	login_form.fields['username'].widget.attrs['style'] = 'margin-top: 20px;'
	login_form.fields['password'].widget.attrs['class'] = 'center_h input_field'
	login_form.fields['password'].widget.attrs['style'] = 'margin-top: 5px;'
	return render(request, 'index.html', {'login_form':login_form})

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

def home(request):
	if auth.get_user(request).is_authenticated:
		return HttpResponse("Hello, " + request.user.username)
	else:
		return HttpResponseRedirect('/')
