from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json

from .models import Feedback, Answer
from .forms import FeedbackForm

def index(request, feedback_id):
	_id = feedback_id
	feedback = Feedback.objects.get(id=_id)
	if request.method == "POST":
		form = FeedbackForm(request.POST)
		if form.is_valid():
			data = []
			for i in request.POST.keys():
				if i != 'csrfmiddlewaretoken':
					data.append([i, request.POST[i]])
			Answer.objects.create(feedback_rel=feedback, data=json.dumps(data))
			return HttpResponseRedirect('/feedbacks/thanks/')
	form = FeedbackForm(data=json.loads(feedback.data))
	context = {
		'title':'Quality Feedback Service',
		'feedback': form
	}
	return render(request, "form/index.html", context)

def thanks(request):
	return HttpResponse("Thanks for your feedback!")
