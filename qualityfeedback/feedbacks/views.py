from django.shortcuts import render
import json

from .models import Feedback
from .forms import FeedbackForm

def index(request):
	_id = request.GET['id']
	feedback = Feedback.objects.get(id=_id)
	feedback_forms = []
	form = FeedbackForm(data=json.loads(feedback.data))
	feedback_forms.append(form)
	context = {
		'title':'Quality Feedback Service',
		'feedback': feedback_forms[0]
	}
	return render(request, "form/index.html", context)
