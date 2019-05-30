from django.test import TestCase

from home.models import Feedback


class FeedbackTestCase(TestCase):

    def create_feedback(self):
        from home.tests.helper import create_feedback as cf
        return cf()

    def test_can_make_feedback(self):
        fb = self.create_feedback()

        self.assertIsInstance(fb, Feedback)

        expected = f'Feedback {fb.name} @ {fb.datetime}'

        self.assertEqual(fb.__str__(), expected)
        self.assertEqual(fb.__repr__(), expected)
