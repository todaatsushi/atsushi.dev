from django.db import models

from PIL import Image


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

    # Index Screenshot
    preview = models.ImageField(default='default.png', upload_to='thumbnails')
    header = models.ImageField(default='default.png', upload_to='headers')

    def __repr__(self):
        return f'{self.project.name} - Specs'

    def __str__(self):
        return f'{self.project.name} - Specs'

    def save(self, *args, **kwargs):
        super().save()


        preview = Image.open(self.preview.path)
        header = Image.open(self.header.path)

        preview.save(self.preview.path)
        header.save(self.header.path)
