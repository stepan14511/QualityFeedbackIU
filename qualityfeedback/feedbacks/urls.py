"""qualityfeedback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from . import views

# A particular feedback form is going to appear if you
# type url ending with /feedbacks/feedback/?id=<feedback_id>
# where <feedback_id> is the id of a particular feedback.
# You can check feedback id in Django Administration Page.
urlpatterns = [
    url(r'^feedback/(?P<feedback_id>\d+)/$', views.index, name='index'),
    url(r'^thanks/$', views.thanks, name='thanks'),
]
