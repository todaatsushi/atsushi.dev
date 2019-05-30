from django.test import TestCase

from work.models import Project, ProjectSpecs


class ProjectTestCase(TestCase):

    def create_project(self):
        from work.tests.helper import create_project as cp
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
        from work.tests.helper import create_project as cp
        return cp()

    def test_project_specs_created(self):
        project = self.create_project()
        self.assertIsInstance(project.projectspecs, ProjectSpecs)

    def test_project_specs_names(self):
        project = self.create_project()
        self.assertEqual(project.projectspecs.__repr__(), 'Test - Specs')
        self.assertEqual(project.projectspecs.__str__(), 'Test - Specs')

    
