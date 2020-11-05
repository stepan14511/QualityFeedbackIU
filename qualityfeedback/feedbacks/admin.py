from django.contrib import admin
from .models import Feedback, FeedbackAdmin, Answer

admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Answer)
