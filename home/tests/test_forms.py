from django.test import TestCase

from home.forms import ContactForm


class CreateFeedback(TestCase):

    def create_feedback(self):
        from home.tests.helper import create_feedback as cf
        return cf()

    def test_projects_form_can_validate_valid_info(self):
        data = self.create_feedback().__dict__
        del data['_state']
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())

    def test_project_form_can_detect_invalid_data(self):
        data = self.create_feedback().__dict__
        del data['_state']

        # Name is required
        data['name'] = ''

        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())