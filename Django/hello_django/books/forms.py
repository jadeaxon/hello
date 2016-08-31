# from django import newforms as forms
from django import forms


TOPIC_CHOICES = (
	('general', 'General enquiry'),
	('bug', 'Bug report'),
	('suggestion', 'Suggestion'),
)

# Defines a user feedback form.
# For the most part it looks like you associate a type of data field with a widget that
# will allow user to view/edit that data.  There is a default widget for each field type.
# These field types appear to be the same as those used to define the data model.
class FeedbackForm(forms.Form):
	topic = forms.ChoiceField(choices=TOPIC_CHOICES)
	# message = forms.CharField()
	message = forms.CharField(widget=forms.Textarea(), initial='Your feedback.') # Don't use default widget.
	sender = forms.EmailField(required=False)


	# You do validation by adding 'clean_<field>' methods.  So, it's a naming convention hook.
	# Either raise a forms.ValidationError or return the cleansed version of the data.
	def clean_message(self):
		message = self.cleaned_data.get('message', '')
		words = len(message.split())
		if words < 4:
			raise forms.ValidationError("Not enough words!")
		return message

