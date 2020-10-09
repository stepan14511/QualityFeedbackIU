from django.contrib import admin
from .models import Question, AnswerText, AnswerChoice, AnswerValue

# Register your models here.
admin.site.register(Question)
admin.site.register(AnswerText)
admin.site.register(AnswerChoice)
admin.site.register(AnswerValue)