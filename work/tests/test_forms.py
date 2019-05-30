from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from work.forms import CreateUpdateProject, CreateUpdateSpecs


class CreateProject(TestCase):

    def create_project(self):
        from work.tests.helper import create_project as cp
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
        from work.tests.helper import create_project as cp
        return cp()

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
        
        
