from django.db import models
from django.conf import settings

from PIL import Image
import re
import pathlib
import os


class Project(models.Model):
    # Descriptive Info
    name = models.CharField(max_length=100)
    url_slug = models.CharField(max_length=100, default='')
    description = models.TextField(null=True)
    link = models.CharField(null=True, max_length=100)
    repository = models.CharField(max_length=100)

    # Technical Info
    languages = models.TextField(null=True)
    stack = models.TextField(null=True)
    hosting = models.CharField(max_length=100, null=True)

    # Status
    current = models.BooleanField(default=False)
    public = models.BooleanField(default=False)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def generate_slug(self):
        # Make valid URL_SLUG
        slug = self.name.lower()
        slug = slug.replace(" ", "-")
        slug = re.sub(r'[^a-zA-Z0-9-]', '', slug)

        self.url_slug = slug

    def get_languages(self):
        return self.languages.split(',')

    def get_stack(self):
        return self.stack.split(',')

    def set_current(self, bool):
        self.current = bool

    def set_public(self, bool):
        self.public = bool


class ProjectSpecs(models.Model):
    project = models.OneToOneField(
        Project,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    technical_summary=models.TextField(default='To be added.')
    best_features=models.TextField(default='To be added.')
    future_plans=models.TextField(default='To be added.')
    things_learned=models.TextField(default='To be added.')

    # Index Screenshots
    preview = models.ImageField(default='default.png', upload_to='previews')
    header = models.ImageField(default='default.png', upload_to='headers')

    def __repr__(self):
        return f'{self.project.name} - Specs'

    def __str__(self):
        return f'{self.project.name} - Specs'

    def save(self, *args, **kwargs):
        """
        Save images directly to the file system.
        """
        super().save()

        preview = Image.open(self.preview.path)
        header = Image.open(self.header.path)

        preview.save(self.preview.path)
        header.save(self.header.path)
