from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings

import pathlib
import os

from work.tests.helper import create_project as cp
from work.tests.helper import create_dummy_image as img
from work.models import Project, ProjectSpecs
from work.forms import CreateUpdateSpecs


class ProjectTestCase(TestCase):

    def testing_media(self):
        return self.settings(MEDIA_ROOT=os.path.join(settings.PROJECT_DIR, 'test_media'))

    def setUp(self):
        with self.testing_media():
            self.project = cp()

    def test_can_make_project(self):
        self.assertIsInstance(self.project, Project)
        self.assertEqual(self.project.__repr__(), self.project.name)
        self.assertEqual(self.project.__str__(), self.project.name)

    def test_project_get_lang(self):
        expected_langs = ['JavaScript', 'C']
        self.assertEqual(expected_langs, self.project.get_languages())

    def test_project_get_stack(self):
        expected_stack = ['React', 'Node']
        self.assertEqual(expected_stack, self.project.get_stack())

    def test_project_set_current(self):
        self.assertFalse(self.project.current)

        self.project.set_current(True)
        self.assertTrue(self.project.current)

    def test_project_set_public(self):
        self.assertFalse(self.project.public)

        self.project.set_public(True)
        self.assertTrue(self.project.public)


class ProjectSpecsTestCase(TestCase):

    def testing_media(self):
        return self.settings(MEDIA_ROOT=os.path.join(settings.PROJECT_DIR, 'test_media'))

    def setUp(self):
        with self.testing_media():
            self.project = cp()
            self.specs = self.project.projectspecs
            self.data = self.specs.__dict__

    def create_image(self, name='test.png'):
        return img(name)

    def test_project_specs_created(self):
        self.assertIsInstance(self.specs, ProjectSpecs)

    def test_project_specs_names(self):
        self.assertEqual(self.specs.__repr__(), 'Test - Specs')
        self.assertEqual(self.specs.__str__(), 'Test - Specs')

    def test_images_are_deleted_on_instance_delete(self):

        with self.testing_media():
            # https://stackoverflow.com/a/34276961
            img = self.create_image()

            self.data['preview'] = img
            self.data['header'] = img

            form = CreateUpdateSpecs(instance=self.specs, data=self.data)
            self.assertTrue(form.is_valid())

            form.save()

            test_image_paths = [
                pathlib.Path(os.path.join(settings.MEDIA_ROOT, 'previews/test.png')),
                pathlib.Path(os.path.join(settings.MEDIA_ROOT, 'headers/test.png')),
            ]

            # Check files were uploaded
            for p in test_image_paths:
                self.assertTrue(p.is_file())

            Project.objects.first().delete()

            # Check files were deleted
            for p in test_image_paths:
                if p.is_file():
                    p.unlink()
                    raise AssertionError('File has not been deleted.')
