from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

from .models import Course

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
	user = auth.get_user(request)
	if user.is_authenticated:
		if user.role == 'professor':
			professors_courses = get_professors_courses(user)

			
			return render(request, 'home/professor.html', {'courses_names': professors_courses})
		else:
			return HttpResponse("Hello, " + request.user.username)
	else:
		return HttpResponseRedirect('/')

def get_professors_courses(professor):
	professors_courses = []
	for course in Course.objects.all():
		if course.professor == professor:
			professors_courses.append(course.course_name)
	return professors_courses