from django import forms

from work.models import Project


class CreateUpdateProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name', 'description', 'link', 'repository', 'languages', 'stack', 'hosting',
            'public', 'current',
        ]
        widgets = {
            'name': forms.TextInput(),
            'description': forms.Textarea(attrs={
                'rows': 5,
            }),
            'link': forms.URLInput(),
            'repository': forms.URLInput(),
            'languages': forms.Textarea(attrs={
                'rows': 2,
            }),
            'stack': forms.Textarea(attrs={
                'rows': 2,
            }),
            'hosting': forms.TextInput(),
            'public': forms.CheckboxInput(),
            'current': forms.CheckboxInput(),
        }
