from django.shortcuts import render
from django.http import HttpResponseRedirect
import json

from django.contrib import auth

from .models import Feedback, Answer
from .forms import FeedbackForm

def index(request, feedback_id):
	user = auth.get_user(request)
	if user.is_authenticated:
		if user.role == 'professor':
			feedback = Feedback.objects.get(id=feedback_id)
			answers = []
			for answer in Answer.objects.all():
				if answer.feedback_rel == feedback:
					answers.append(json.loads(answer.data))
			context = {
				'feedback_name' : feedback.name,
				'feedback_questions' : json.loads(feedback.data),
				'answers' : answers
			}
			return render(request, "feedback_data/feedback_data.html", context)
		else:
			_id = feedback_id
			feedback = Feedback.objects.get(id=_id)
			if request.method == "POST":
				form = FeedbackForm(request.POST)
				if form.is_valid():
					data = []
					for i in request.POST.keys():
						if i != 'csrfmiddlewaretoken':
							data.append([i, request.POST.getlist(i)])
					Answer.objects.create(feedback_rel=feedback, data=json.dumps(data))
					return HttpResponseRedirect('/feedbacks/thanks/')
			form = FeedbackForm(data=json.loads(feedback.data))
			context = {
				'title': 'Quality Feedback Service',
				'name': feedback.name,
				'feedback': form
			}
			return render(request, "form/index.html", context)
	else:
		return HttpResponseRedirect('/')

def thanks(request):
	return render(request, 'form/done.html')
