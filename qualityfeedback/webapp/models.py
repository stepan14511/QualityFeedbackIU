from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
	use_in_migrations = True
	def _create_user(self, email, username, first_name, last_name, password, role):
		"""
		Create and save a user with the given username, email,
		full_name, and password.
		"""
		if not email:
			raise ValueError('The given email must be set')
		if not username:
			raise ValueError('The given username must be set')
		if not first_name:
			raise ValueError('The given first name must be set')
		if not last_name:
			raise ValueError('The given last name must be set')
		email = self.normalize_email(email)
		username = self.model.normalize_username(username)
		user = self.model(
			email=email, username=username, first_name=first_name, last_name=last_name, role=role
		)
		user.set_password(password)
		return user

	def create_user(self, email, username, first_name, last_name, password=None, role="student"):
		user = self._create_user(email, username, first_name, last_name, password, role)
		user.is_admin = False
		user.is_staff = False
		user.is_superuser = False
		user.save(using=self._db)
		return user
		
	def create_superuser(self, email, username, first_name, last_name, password, role="admin"):
		user = self._create_user(email, username, first_name, last_name, password, role)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class User(AbstractBaseUser, PermissionsMixin):
	ROLES = (
		('admin', 'admin of the service'),
		('student', 'student of a Uni'),
		('professor', 'professor of a Uni'),
	)
	username_validator = UnicodeUsernameValidator()
	username = models.CharField(
		max_length=150,
		unique=True,
		validators=[username_validator],
	)
	email = models.EmailField(unique=True)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)

	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
	role = models.CharField(max_length=20, choices=ROLES, blank=True)

	objects = UserManager()
	def __str__(self):
		return self.email
	def get_short_name(self):
		return self.email
	def get_full_name(self):
		return self.first_name + ' ' + self.last_name
	def get_role(self):
		return self.role

class Course(models.Model):
	course_name = models.TextField();
	professor = models.ForeignKey(User, on_delete=models.PROTECT)
	groups = models.ManyToManyField('Group', blank=True)

class Group(models.Model):
	course_rel = models.ForeignKey(Course, on_delete=models.CASCADE)
	group_name = models.CharField(max_length=20, blank=True)
	students = models.ManyToManyField('User', blank=True)
