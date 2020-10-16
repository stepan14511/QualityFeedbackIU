from django.shortcuts import render
import json

from .models import Feedback
from .forms import FeedbackForm

def index(request):
	feedbacks = Feedback.objects.all()
	feedback_forms = []
	for f in feedbacks:
		form = FeedbackForm(data=json.loads(f.data))
		feedback_forms.append(form)
	context = {
		'title':'Quality Feedback Service',
		'feedback': feedback_forms[1]
	}
	return render(request, "form/index.html", context)
