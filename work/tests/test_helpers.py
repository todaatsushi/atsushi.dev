from django.test import TestCase
from django.conf import settings

import os

from work.tests.helper import create_project as cp
from work.models import Project
from work.helper import get_current_or_dummy, unpack


class HelperFuncsTestCase(TestCase):

    def testing_media(self):
        return self.settings(MEDIA_ROOT=os.path.join(settings.PROJECT_DIR, 'test_media'))

    def setUp(self):
        with self.testing_media():
            self.project = cp()

    def test_unpack(self):
        test_input = [
            'item1,item2,item3',
            'item4,item2,item3',
            'item5',
            ]

        expected_output = [
            'item1', 'item2', 'item3',
            'item4', 'item5'
        ]

        # If all of unpack is in expected, it is a subset
        self.assertTrue(
            set(unpack(test_input)).issubset(expected_output)
        )

    def test_get_current_or_dummy(self):
        # there are no current flagged projects
        self.assertFalse(
            isinstance(get_current_or_dummy(), Project)
        )

        # Set current to True -  retrieves current?
        self.project.current = True
        self.project.save()

        self.assertIsInstance(get_current_or_dummy(), Project)