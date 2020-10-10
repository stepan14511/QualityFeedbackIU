from .models import AnswerText, AnswerValue, AnswerChoice
from django.forms import ModelForm, Textarea, Select, NumberInput

class AnswerTextForm(ModelForm):
    class Meta:
        model = AnswerText
        fields = ["answer"]
        widgets = {
            "answer": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write an answer'
            }),
        }

class AnswerChoiceForm(ModelForm):
    class Meta:
        model = AnswerChoice
        fields = ["answer"]
        widgets = {
            "answer": Select(choices=AnswerChoice.CHOICES),
        }

class AnswerValueForm(ModelForm):
    class Meta:
        model = AnswerValue
        fields = ["answer"]
        widgets = {
            "answer": NumberInput(),
        }