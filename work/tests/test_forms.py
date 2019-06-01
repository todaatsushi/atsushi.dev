from django.test import TestCase
from django.test.utils import override_settings
from django.urls import reverse
from django.conf import settings

import pathlib
import os

from work.forms import CreateUpdateProject, CreateUpdateSpecs
from work.tests.helper import create_dummy_image as img
from work.tests.helper import create_project as cp


class CreateProject(TestCase):

    def setUp(self):
        self.project = cp()
        self.data = self.project.__dict__

    def test_projects_form_can_validate_valid_info(self):
        del self.data['_state']
        form = CreateUpdateProject(data=self.data)
        self.assertTrue(form.is_valid())

    def test_project_form_can_detect_invalid_data(self):
        del self.data['_state']

        # Name is required
        self.data['name'] = ''

        form = CreateUpdateProject(data=self.data)
        self.assertFalse(form.is_valid())

    def test_updating_project_works(self):

        form = CreateUpdateProject(instance=self.project, data=self.data)
        self.assertTrue(form.is_valid())

        self.assertTrue(self.project.name == 'Test')

        form.data['name'] = 'New name'

        form.save()
        self.assertTrue(self.project.name == 'New name')


class UpdateProjectSpecs(TestCase):

    def setUp(self):
        self.project = cp()
        self.specs = self.project.projectspecs
        self.data = self.specs.__dict__

    def testing_media(self):
        return self.settings(MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'test_media'))

    def create_image(self, name='test.png'):
        return img(name)

    def test_specs_form_can_validate_valid_info(self):
        del self.data['_state']

        form = CreateUpdateSpecs(data=self.data)
        self.assertTrue(form.is_valid())

    def test_specs_form_can_detect_invalid_data(self):
        del self.data['_state']

        self.data['best_features'] = ''

        form = CreateUpdateSpecs(data=self.data)
        self.assertFalse(form.is_valid())

    def test_updating_specs_works(self):
        form = CreateUpdateSpecs(instance=self.specs, data=self.data)
        self.assertTrue(form.is_valid())

        # Current default entry for specs field
        self.assertTrue(self.specs.technical_summary == 'To be added.')

        form.data['technical_summary'] = 'Test summary'

        form.save()
        self.assertTrue(self.specs.technical_summary == 'Test summary')

    def test_files_upload_correctly(self):
        # https://stackoverflow.com/a/34276961
        with self.testing_media():
            # Check for default image
            self.assertEqual(self.specs.preview.url, '/media/default.png')

            # New PIL Image
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

            for p in test_image_paths:
                self.assertTrue(p.is_file())

            # Delete test file
            for p in test_image_paths:
                p.unlink()

    def test_old_images_are_deleted_on_on_instance_update(self):
        with self.testing_media():
            img = self.create_image()

            # First iteration - from default images to new ones (i.e. save new files on system)
            self.data['preview'] = img
            self.data['header'] = img

            form = CreateUpdateSpecs(instance=self.specs, data=self.data)
            self.assertTrue(form.is_valid())

            form.save()
            
            test_image_paths = [
                pathlib.Path(os.path.join(settings.MEDIA_ROOT, 'previews/test.png')),
                pathlib.Path(os.path.join(settings.MEDIA_ROOT, 'headers/test.png')),
            ]

            for p in test_image_paths:
                self.assertTrue(p.is_file())

            # Second iteration - upload new images and set into instance fields (i.e. render old images redundant. Old files should now delete.)
            img2 = self.create_image('test2.png')

            self.data['preview'] = img2
            self.data['header'] = img2

            form = CreateUpdateSpecs(instance=self.specs, data=self.data)
            self.assertTrue(form.is_valid())

            form.save()
            
            test_image_paths2 = [
                pathlib.Path(os.path.join(settings.MEDIA_ROOT, 'previews/test2.png')),
                pathlib.Path(os.path.join(settings.MEDIA_ROOT, 'headers/test2.png')),
            ]

            # Check new files exist
            for p in test_image_paths2:
                self.assertTrue(p.is_file())

            # Check old files are deleted
            for p in test_image_paths:
                self.assertFalse(p.is_file())
