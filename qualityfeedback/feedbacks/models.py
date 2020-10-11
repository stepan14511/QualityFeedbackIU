from django.db import models
from webapp.models import User, Course, Group

class Feedback(models.Model):
	group_rel = models.ForeignKey(Course, on_delete=models.CASCADE)
	data = models.TextField()

class Answer(models.Model):
	feedback_rel = models.ForeignKey(Feedback, on_delete=models.CASCADE)
	data = models.TextField()
