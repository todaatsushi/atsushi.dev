from django import forms

from work.models import Project, ProjectSpecs


class CreateUpdateProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name', 'description', 'one_line', 'link', 'repository', 'languages', 'stack', 'extra_tags',
            'hosting', 'public', 'current', 'best',
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
            'extra_tags': forms.Textarea(attrs={
                'rows': 2,
            }),
            'hosting': forms.TextInput(),
            'public': forms.CheckboxInput(),
            'current': forms.CheckboxInput(),
        }


class CreateUpdateSpecs(forms.ModelForm):
    class Meta:
        model = ProjectSpecs
        fields = [
            'technical_summary', 'best_features', 'future_plans',
            'things_learned', 'preview', 'header',
        ]
