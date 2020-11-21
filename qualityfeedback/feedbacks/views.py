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
			raw_answers = []
			for answer in Answer.objects.all():
				if answer.feedback_rel == feedback:
					raw_answers.append(json.loads(answer.data))
			raw_feedback_questions = json.loads(feedback.data)
			print(compose_feedback_data(raw_feedback_questions, raw_answers))
			context = {
				'feedback_name' : feedback.name,
				'feedback_data' : compose_feedback_data(raw_feedback_questions, raw_answers)
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

def compose_feedback_data(feedback_questions, raw_answers):
	answers = []
	for feedback_question in feedback_questions:
		answer = []
		answer.append(feedback_question[1])
		for raw_answer in raw_answers:
			for raw_answer_to_question in raw_answer:
				if raw_answer_to_question[0] == feedback_question[0]:
					if feedback_question[2] == "text":
						text_answer = []
						text_answer.append(raw_answer_to_question[1][0])
						answer.append(text_answer)
					elif feedback_question[2] == "single_choice":
						choice_number = int(raw_answer_to_question[1][0])
						single_choice_answer = []
						single_choice_answer.append(feedback_question[3][choice_number])
						answer.append(single_choice_answer)
					elif feedback_question[2] == "multiple_choice":
						multiple_choice_answers = []
						for raw_choice_number in raw_answer_to_question[1]:
							choice_number = int(raw_choice_number)
							multiple_choice_answers.append(feedback_question[3][choice_number])
						answer.append(multiple_choice_answers)
					elif feedback_question[2] == "slider":
						answer.append(list(raw_answer_to_question[1][0]))
		answers.append(answer)
	return answers

def thanks(request):
	return render(request, 'form/done.html')
