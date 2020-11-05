from django.shortcuts import render

from .forms import CreateFeedbackForm

def index(request):
	# _id = feedback_id
	# feedback = Feedback.objects.get(id=_id)
	# if request.method == "POST":
	# 	form = FeedbackForm(request.POST)
	# 	if form.is_valid():
	# 		data = []
	# 		for i in request.POST.keys():
	# 			if i != 'csrfmiddlewaretoken':
	# 				data.append([i, request.POST.getlist(i)])
	# 		Answer.objects.create(feedback_rel=feedback, data=json.dumps(data))
	# 		return HttpResponseRedirect('/feedbacks/thanks/')

	context = {
		'title': 'Create a Feedback Form',
		'form': CreateFeedbackForm()
	}
	return render(request, "form_creation/index.html", context)