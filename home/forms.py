from django import forms

from home.models import Feedback


class ContactForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'name', 'email', 'message', 'score'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Message',
                'rows': 10,
            })
        }
        help_texts = {
            'score': 'Score out of 5 based on my hireability having seen my site.'
        }
