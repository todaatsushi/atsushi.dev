from django.test import TestCase

from home.models import Feedback, SongPick


class FeedbackTestCase(TestCase):

    def create_feedback(self):
        from home.tests.helper import create_feedback as cf
        return cf()

    def test_can_make_feedback(self):
        fb = self.create_feedback()
        self.assertIsInstance(fb, Feedback)

    def test_feedback_appears_correctly(self):
        fb = self.create_feedback()
        expected = f'Feedback {fb.name} @ {fb.datetime}'
        self.assertEqual(fb.__str__(), expected)
        self.assertEqual(fb.__repr__(), expected)


class SongPickTestCase(TestCase):

    def create_songpick(self):
        return SongPick.objects.create(name='Great Song', artist='Great Artist')

    def test_can_make_songpick(self):
        s = self.create_songpick()
        self.assertIsInstance(s, SongPick)
    
    def test_songpick_appears_correctly(self):
        s = self.create_songpick()
        expected = f'{s.name} by {s.artist}'
        self.assertEqual(s.__str__(), expected)
        self.assertEqual(s.__repr__(), expected)
