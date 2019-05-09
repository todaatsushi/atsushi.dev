from django import forms

from work.models import Project


class CreateUpdateProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name', 'description', 'link', 'repository', 'languages', 'stack', 'hosting',
        ]
        
