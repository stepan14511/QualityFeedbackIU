from django import forms

from webapp.models import Group

class CreateFeedbackForm(forms.Form):
    name = forms.CharField(label="Title", widget=forms.TextInput(attrs={'class': 'ftype_text'}))

    CHOICES = []
    for group in Group.objects.all():
        CHOICES.append((group, group))

    group_rel = forms.ChoiceField(label="Group rel", choices=CHOICES, widget=forms.Select(attrs={'class': 'ftype_single_choice'}))