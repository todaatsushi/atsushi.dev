from django.db import models


class Project(models.Model):
    # Descriptive Info
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    link = models.CharField(null=True, max_length=100)
    repository = models.CharField(max_length=100)

    # Technical Info
    languages = models.TextField()
    hosting = models.CharField(max_length=100, null=True)
