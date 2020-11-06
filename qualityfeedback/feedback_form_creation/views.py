from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import CreateFeedbackForm
from feedbacks.models import Feedback
from webapp.models import Group

def index(request):

	if request.method == "POST":
		form = CreateFeedbackForm(request.POST)
		if form.is_valid():
			data = []
			for i in request.POST.keys():
				if i != 'csrfmiddlewaretoken':
					data.append(request.POST.get(i))
			title = data[0]
			group = Group.objects.get(group_name=data[1])
			questions = data[2]
			Feedback.objects.create(name=title, group_rel=group, data=questions)
			return HttpResponseRedirect('/create/thanks/')

	context = {
		'title': 'Create a Feedback Form',
		'form': CreateFeedbackForm()
	}
	return render(request, "form_creation/index.html", context)

def thanks(request):
	return render(request, 'form_creation/done_form_creation.html')