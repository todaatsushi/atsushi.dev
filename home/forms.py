from django import forms

from home.models import Feedback


class ContactForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'name', 'email', 'message', 'score'
        ]