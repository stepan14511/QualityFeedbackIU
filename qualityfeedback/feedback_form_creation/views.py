from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.contrib import auth

from .forms import CreateFeedbackForm
from feedbacks.models import Feedback
from webapp.models import Group

def index(request):
	user = auth.get_user(request)
	if user.is_authenticated:
		if request.method == "POST":
			form = CreateFeedbackForm(request.POST)
			if form.is_valid():
				title = request.POST.get("name")
				group = Group.objects.get(group_name=request.POST.get("group_rel"))
				questions = []
				for i in range(1, int(request.POST.get("number_of_questions")) + 1):
					q_type = request.POST.get("question_"+str(i)+"_type")
					question = [str(i), request.POST.get("question_"+str(i)+"_name"), q_type]

					if q_type in ["single_choice", "multiple_choice"]:
						answers = []
						for j in range(1, int(request.POST.get("question_"+str(i)+"_num_answers")) + 1):
							answers.append(request.POST.get("question_"+str(i)+"_answer_"+str(j)))
						question.append(answers)

					if q_type == "slider":
						ranges = [int(request.POST.get("question_"+str(i)+"_begin")), int(request.POST.get("question_"+str(i)+"_end")), int(request.POST.get("question_"+str(i)+"_step"))]
						question.append(ranges)

					questions.append(question)

				feedback = Feedback.objects.create(name=title, group_rel=group, data=str(questions).replace("\'", "\""))


				return HttpResponseRedirect('/create/thanks/?id='+str(feedback.id))

		context = {
			'title': 'Create a Feedback Form',
			'form': CreateFeedbackForm()
		}
		return render(request, "form_creation/index.html", context)
	else:
		return HttpResponseRedirect('/')

def thanks(request):
	user = auth.get_user(request)
	if user.is_authenticated:
		f_id = request.GET['id']
		link = "http://127.0.0.1:8000/feedbacks/feedback/" + str(f_id)
		context = {
			'link' : link
		}
		return render(request, 'form_creation/done_form_creation.html', context)
	else:
		return HttpResponseRedirect('/')