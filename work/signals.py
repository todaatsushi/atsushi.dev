from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.core.files.storage import default_storage
from django.conf import settings

import os

from work.models import Project, ProjectSpecs


# Ensure project has url_slug on creation
@receiver(post_save, sender=Project)
def ensure_slug_exists(sender, instance, created, **kwargs):
    if created:
        if not instance.url_slug:
            instance.generate_slug()
            instance.save()


# when post_save is called, make obj
@receiver(post_save, sender=Project)
def create_project_specs(sender, instance, created, **kwargs):
    if created:
        ProjectSpecs.objects.create(project=instance)


# Delete preview and header files after project delete
# https://stackoverflow.com/questions/55480222/remove-images-from-media-folder-after-deleting-blog-post
@receiver(post_delete, sender=Project)
# delete old preview and header shots when specs is updated
@receiver(post_save, sender=ProjectSpecs)
def delete_unused_image_files(sender, instance, **kwargs):

    media_root = settings.MEDIA_ROOT
    
    # Get all current used previews & headers
    in_use = [
        spec.preview.url.replace('/media/', f'{media_root}/') for spec in ProjectSpecs.objects.all()
        ] + [
        spec.header.url.replace('/media/', f'{media_root}/') for spec in ProjectSpecs.objects.all()
        ]

    # Image locations
    header_dir = os.path.join(media_root, 'headers')
    prev_dir = os.path.join(media_root, 'previews')

    all_headers = [f'{header_dir}/{file}' for file in os.listdir(header_dir)]
    all_prevs = [f'{prev_dir}/{file}' for file in os.listdir(prev_dir)]
    all_imgs = all_headers + all_prevs

    not_needed = [path for path in all_imgs if path not in in_use]
    
    for path in not_needed:
        if path:
            default_storage.delete(path)


