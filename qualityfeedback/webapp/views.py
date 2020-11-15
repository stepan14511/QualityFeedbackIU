from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import LoginForm

def index(request):
	login_form = LoginForm()
	return render(request, 'index.html', {'login_form':login_form})
