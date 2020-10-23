from django.shortcuts import render

def index(request):
	context = {
		'title': 'Create a Feedback Form',
	}
	return render(request, "form_creation/index.html", context)