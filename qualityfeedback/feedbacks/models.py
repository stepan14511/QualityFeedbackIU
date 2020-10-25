from django.contrib import admin
from django.db import models
from webapp.models import User, Course, Group

class Feedback(models.Model):
	group_rel = models.ForeignKey(Group, on_delete=models.CASCADE)
	name = models.CharField(default='', max_length=256)
	data = models.TextField()

class FeedbackAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class Answer(models.Model):
	feedback_rel = models.ForeignKey(Feedback, on_delete=models.CASCADE)
	data = models.TextField()
