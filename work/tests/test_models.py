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

    def create_project(self):
        return cp()

    def test_can_make_project(self):
        project = self.create_project()

        self.assertIsInstance(project, Project)
        self.assertEqual(project.__repr__(), project.name)
        self.assertEqual(project.__str__(), project.name)

    def test_project_get_lang(self):
        project = self.create_project()

        expected_langs = ['JavaScript', 'C']
        self.assertEqual(expected_langs, project.get_languages())

    def test_project_get_stack(self):
        project = self.create_project()

        expected_stack = ['React', 'Node']
        self.assertEqual(expected_stack, project.get_stack())

    def test_project_set_current(self):
        project = self.create_project()

        self.assertFalse(project.current)

        project.set_current(True)
        self.assertTrue(project.current)

    def test_project_set_public(self):
        project = self.create_project()

        self.assertFalse(project.public)

        project.set_public(True)
        self.assertTrue(project.public)


class ProjectSpecsTestCase(TestCase):

    def create_project(self):
        return cp()

    def create_image(self):
        return img()

    def test_project_specs_created(self):
        project = self.create_project()
        self.assertIsInstance(project.projectspecs, ProjectSpecs)

    def test_project_specs_names(self):
        project = self.create_project()
        self.assertEqual(project.projectspecs.__repr__(), 'Test - Specs')
        self.assertEqual(project.projectspecs.__str__(), 'Test - Specs')

    def test_images_are_deleted_on_instance_delete(self):
        # https://stackoverflow.com/a/34276961
        specs = self.create_project().projectspecs
        data = specs.__dict__

        img = self.create_image()

        data['preview'] = img
        data['header'] = img

        form = CreateUpdateSpecs(instance=specs, data=data)
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
