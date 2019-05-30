from django.utils import timezone

from home.models import Feedback


def create_feedback():
    return Feedback.objects.create(
        name='Atsushi',
        email='test@mail.com',
        message='This is a test message!',
        score=5,
        datetime=timezone.now()
            )