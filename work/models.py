from django.db import models


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

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
