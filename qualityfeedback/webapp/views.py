from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

from .models import Course, Group
from feedbacks.models import Feedback

def index(request):
	login_form = AuthenticationForm()
	login_form.fields['username'].widget.attrs['class'] = 'center_h input_field'
	login_form.fields['username'].widget.attrs['style'] = 'margin-top: 20px;'
	login_form.fields['username'].widget.attrs['placeholder'] = 'Email'
	login_form.fields['password'].widget.attrs['class'] = 'center_h input_field'
	login_form.fields['password'].widget.attrs['style'] = 'margin-top: 5px;'
	login_form.fields['password'].widget.attrs['placeholder'] = 'Password'
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
            print(get_professors_feedbackforms_by_group(user))
            context = {
                'feedbackforms_pool' : get_professors_feedbackforms(user),
                'courses': get_professors_courses(user),
                'feedbackforms_by_group' : get_professors_feedbackforms_by_group(user)
            }
            return render(request, 'home/professor.html', context)
        elif user.role == 'student':
            context ={
                'feedbackforms': get_students_feedbackforms(user)
            }
            return render(request, 'home/student.html', context)
        else:
            return HttpResponse("Hello, " + request.user.username)
    else:
        return HttpResponseRedirect('/')

def get_professors_courses(professor):
    professors_courses = []
    for course in Course.objects.all():
        if course.professor == professor:
            professors_courses.append(course)
    return professors_courses

def get_professors_feedbackforms(professor):
    feedbackforms = []
    for feedbackform in Feedback.objects.all():
        if feedbackform.group_rel.course_rel.professor == professor:
            feedbackforms.append(feedbackform)
    return feedbackforms

def get_professors_feedbackforms_by_group(professor):
    feedbackforms = []
    for group in Group.objects.all():
        if group.course_rel.professor == professor:
            feedbackforms_for_group = []
            for feedbackform in Feedback.objects.all():
                if feedbackform.group_rel == group:
                    feedbackforms_for_group.append(feedbackform)
            feedbackforms.append((group, feedbackforms_for_group))
    return feedbackforms

def get_students_feedbackforms(student):
    feedbackforms = []
    groups = []
    for group in Group.objects.all():
        for stud in group.students.all():
            if stud == student:
                groups.append(group)
                continue
    for feedbackform in Feedback.objects.all():
        for group in groups:
            if feedbackform.group_rel == group:
                feedbackforms.append(feedbackform)
    return feedbackforms
