from django.shortcuts import render, redirect
from .models import Question
from .forms import AnswerTextForm, AnswerChoiceForm, AnswerValueForm

def index(request):

    # here we get all the questions from the database
    # in this case the questions
    questions = Question.objects.all()

    if request.method == 'POST':
        # TODO: Implement data saving to the database
        # saving happens something like this
        # forms = [AnswerForm(request.POST) for i in range(questions.count())]
        # for form in forms:
        #     if form.is_valid():
        #         form.save()
        return redirect('done')

    answer_forms = []

    for question in questions:
        if question.answer_type == "TEXT":
            answer_forms.append(AnswerTextForm())
        elif question.answer_type == "CHOICE":
            answer_forms.append(AnswerChoiceForm())
        else:
            answer_forms.append(AnswerValueForm())

    context = {
        'title':'Quality Feedback Service',
        'questions': questions,
        'answer_forms':answer_forms
    }
    return render(request, "form/index.html", context)

def done(request):
    return render(request, "form/done.html")
