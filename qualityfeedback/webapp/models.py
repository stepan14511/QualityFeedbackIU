from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
	ROLES = (
		('student', 'student of a Uni'),
		('professor', 'professor of a Uni'),
	)
	username = models.CharField(max_length=40)
	email = models.CharField(max_length=40)
	password_hash = models.CharField(max_length=32)
	role = models.CharField(max_length=20, choices=ROLES, blank=True)

class Course(models.Model):
	course_name = models.TextField();
	professor = models.ForeignKey(User, on_delete=models.PROTECT)
	groups = models.ManyToManyField('Group', blank=True)

class Group(models.Model):
	course_rel = models.ForeignKey(Course, on_delete=models.CASCADE)
	group_name = models.CharField(max_length=20, blank=True)
	students = models.ManyToManyField('User', blank=True)
