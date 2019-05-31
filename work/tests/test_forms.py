from django.test import TestCase
from django.urls import reverse
from django.conf import settings

import pathlib
import os

from work.forms import CreateUpdateProject, CreateUpdateSpecs
from work.tests.helper import create_dummy_image as img
from work.tests.helper import create_project as cp


class CreateProject(TestCase):

    def create_project(self):
        return cp()

    def test_projects_form_can_validate_valid_info(self):
        data = self.create_project().__dict__
        del data['_state']
        form = CreateUpdateProject(data=data)
        self.assertTrue(form.is_valid())

    def test_project_form_can_detect_invalid_data(self):
        data = self.create_project().__dict__
        del data['_state']

        # Name is required
        data['name'] = ''

        form = CreateUpdateProject(data=data)
        self.assertFalse(form.is_valid())

    def test_updating_project_works(self):
        project = self.create_project()
        data = project.__dict__

        form = CreateUpdateProject(instance=project, data=data)
        self.assertTrue(form.is_valid())

        self.assertTrue(project.name == 'Test')

        form.data['name'] = 'New name'

        form.save()
        self.assertTrue(project.name == 'New name')


class UpdateProjectSpecs(TestCase):

    def setUp(self):
        super().setUp()
    
    def create_project(self):
        return cp()

    def create_image(self):
        return img()

    def test_specs_form_can_validate_valid_info(self):
        data = self.create_project().projectspecs.__dict__
        del data['_state']

        form = CreateUpdateSpecs(data=data)
        self.assertTrue(form.is_valid())

    def test_specs_form_can_detect_invalid_data(self):
        data = self.create_project().projectspecs.__dict__
        del data['_state']

        data['best_features'] = ''

        form = CreateUpdateSpecs(data=data)
        self.assertFalse(form.is_valid())

    def test_updating_specs_works(self):
        specs = self.create_project().projectspecs
        data = specs.__dict__

        form = CreateUpdateSpecs(instance=specs, data=data)
        self.assertTrue(form.is_valid())

        self.assertTrue(specs.technical_summary == 'To be added.')

        form.data['technical_summary'] = 'Test summary'

        form.save()
        self.assertTrue(specs.technical_summary == 'Test summary')

    def test_files_upload_correctly(self):
        # https://stackoverflow.com/a/34276961

        specs = self.create_project().projectspecs
        data = specs.__dict__

        # Check for default image
        self.assertEqual(specs.preview.url, '/media/default.png')

         # New PIL Image
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

        for p in test_image_paths:
            self.assertTrue(p.is_file())

        # Delete test file
        for p in test_image_paths:
            p.unlink()
