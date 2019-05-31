from django.core.files.uploadedfile import InMemoryUploadedFile

from work.models import Project

from PIL import Image
from io import BytesIO

def create_project():
    return Project.objects.create(name='Test', url_slug='test', description='test',
            link='http://www.test.com', repository='http://www.test.com',
            languages='JavaScript,C', stack='React,Node', hosting='Heroku',
            current=False, public=False
            )

def create_dummy_image():
    # New PIL Image
    image = Image.new(mode='RGB', size=(200,200))

    # BytesIO obj for saving the image
    image_io = BytesIO()

    # Save the image
    image.save(image_io, 'PNG')

    # Seek to start
    image_io.seek(0)

    return InMemoryUploadedFile(
        image_io, None, 'test.png', 'image/png', len(image_io.getvalue()), None
    )
    