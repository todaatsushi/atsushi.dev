from django.db import models
from django.utils import timezone


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()
    score = models.IntegerField()
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Feedback {self.name} @ {self.datetime}'

    def __repr__(self):
        return f'Feedback {self.name} @ {self.datetime}'


class SongPick(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} by {self.artist}'

    def __repr__(self):
        return f'{self.name} by {self.artist}'

