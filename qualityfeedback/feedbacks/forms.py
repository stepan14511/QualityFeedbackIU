from django import forms
from .RangeSlider import RangeSliderField
# data should be an array with elements - arrays,
# which contain field data to add to the feedback
# Each element is an array with 3 or 4 elements -
# a field name, a question, type of a field and choices, if the type of a field is 'choices_*'
# 
# field types: text, textarea, single_choice, multiple_choice, slider
#
# example:
# data= [
#	["name", "What is your name?", "text"],
#	["who", "Describe you below.", "textarea"],
#	["who_r_u", "Who are you?", "single_choice", ["manager", "developer", "designer"]],
#	["where_r_u", "Where are you from?", "multiple_choice", ["Russia", "Kazan", "Innop"]], 
#	["idk", "slider, wualya", "slider", [5, 8, 0.5]]
#   // [5, 8, 0.5] = [min, max, step]
# ]

class FeedbackForm(forms.Form):
	def __init__(self, *args, **kwargs):
		data_fields = kwargs.pop('data', [])
		super(FeedbackForm, self).__init__(*args, **kwargs)

		for field_info in data_fields:
			if len(field_info) < 3:
				continue
			fname = field_info[0]
			flabel = field_info[1]
			ftype = field_info[2]
			
			if ftype == 'text':
				self.fields[fname] = forms.CharField(label=flabel, widget=forms.TextInput(attrs={'class' : 'ftype_text'}))
			elif ftype == 'textarea':
				self.fields[fname] = forms.CharField(label=flabel, widget=forms.Textarea(attrs={'class' : 'ftype_textarea'}))
			elif ftype == 'single_choice':
				CHOICES = self.get_choices(field_info)
				self.fields[fname] = forms.ChoiceField(label=flabel, choices=CHOICES, widget=forms.Select(attrs={'class' : 'ftype_single_choice'}))
			elif ftype == 'multiple_choice':
				CHOICES = self.get_choices(field_info)
				self.fields[fname] = forms.MultipleChoiceField(label=flabel, widget=forms.CheckboxSelectMultiple(attrs={'class' : 'ftype_multiple_choice'}), choices=CHOICES)
			elif ftype == 'slider':
				self.fields[fname] = RangeSliderField(label=flabel, minimum=field_info[3][0], maximum=field_info[3][1], step=field_info[3][2])

	def get_choices(self, field_info):
		CHOICES = []
		for i in range(len(field_info[3])):
			CHOICES.append((i, field_info[3][i]))
		return CHOICES

