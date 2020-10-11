from django import forms

# data should be an array with elements - arrays,
# which contain field data to add to the feedback
# Each element is an array with 3 or 4 elements -
# a field name, a question, type of a field and choices, if the type of a field is 'choices_*'
# 
# field types: text, textarea, choices_select
#
# example:
# data=[["name", "What is your name?", "text"], ["who", "Who are you?", "choices_select", ["manager", "developer", "designer"]]]
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
				self.fields[fname] = forms.CharField(label=flabel, widget=forms.TextInput)
			elif ftype == 'textarea':
				self.fields[fname] = forms.CharField(label=flabel, widget=forms.Textarea)
			elif ftype == 'choices_select':
				CHOICES = []
				for i in range(len(field_info[3])):
					CHOICES.append((i, field_info[3][i]))
				self.fields[fname] = forms.ChoiceField(label=flabel, choices=CHOICES, widget=forms.Select)
