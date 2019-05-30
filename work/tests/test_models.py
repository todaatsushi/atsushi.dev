from django.test import TestCase

from work.models import Project, ProjectSpecs


class ProjectTestCase(TestCase):
    
    def create_project(self):
        return Project.objects.create(name='Test', url_slug='test', description='test',
                link='http://www.test.com', repository='http://www.test.com',
                languages='JavaScript,C', stack='React,Node', hosting='Heroku',
                current=False, public=False
                )

    def test_can_make_project(self):
        project = self.create_project()

        self.assertIsInstance(project, Project)
        self.assertEqual(project.__repr__(), project.name)
        self.assertEqual(project.__str__(), project.name)

    def test_project_gets_work(self):
        project = self.create_project()

        expected_langs = ['JavaScript', 'C']
        expected_stack = ['React', 'Node']

        self.assertEqual(expected_langs, project.get_languages())
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
        return Project.objects.create(name='Test', url_slug='test', description='test',
                link='http://www.test.com', repository='http://www.test.com',
                languages='JavaScript,C', stack='React,Node', hosting='Heroku',
                current=False, public=False
                )

    def test_project_specs_created(self):
        project = self.create_project()
        self.assertIsInstance(project.projectspecs, ProjectSpecs)

    def test_project_specs_names(self):
        project = self.create_project()
        self.assertEqual(project.projectspecs.__repr__(), 'Test - Specs')
        self.assertEqual(project.projectspecs.__str__(), 'Test - Specs')

    
