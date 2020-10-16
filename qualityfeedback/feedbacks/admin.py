from django.contrib import admin
from .models import Feedback, FeedbackAdmin

admin.site.register(Feedback, FeedbackAdmin)
