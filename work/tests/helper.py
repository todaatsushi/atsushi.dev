from work.models import Project

def create_project():
    return Project.objects.create(name='Test', url_slug='test', description='test',
            link='http://www.test.com', repository='http://www.test.com',
            languages='JavaScript,C', stack='React,Node', hosting='Heroku',
            current=False, public=False
            )