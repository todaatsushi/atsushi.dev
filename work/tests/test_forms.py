from django.test import TestCase

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


class UpdateProjectSpecs(TestCase):
    
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
