from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage

import os
from django.conf import settings

from work.models import Project, ProjectSpecs


# Ensure project has url_slug on creation
@receiver(post_save, sender=Project)
def ensure_slug_exists(sender, instance, created, **kwargs):
    if created:
        if not instance.url_slug:
            instance.generate_slug()
            instance.save()


# when post_save was called
@receiver(post_save, sender=Project)
def create_project_specs(sender, instance, created, **kwargs):
    if created:
        ProjectSpecs.objects.create(project=instance)


# Save new profile after creation
@receiver(post_save, sender=Project)
def save_project_specs(sender, instance, **kwargs):
    instance.projectspecs.save()


# Delete preview and header files after project delete
# https://stackoverflow.com/questions/55480222/remove-images-from-media-folder-after-deleting-blog-post
@receiver(post_delete, sender=Project)
def delete_header_and_preview_after_delete(sender, instance, **kwargs):
    # Get all current used previews & headers
    in_use = [spec.preview.url for spec in ProjectSpecs.objects.all()] + [spec.header.url for spec in ProjectSpecs.objects.all()]

    # Image locations
    header_dir = os.path.join(settings.MEDIA_ROOT, 'headers/')
    prev_dir = os.path.join(settings.MEDIA_ROOT, 'previews/')

    all_headers = [f'{header_dir}/{file}' for file in os.listdir(header_dir)]
    all_prevs = [f'{prev_dir}/{file}' for file in os.listdir(prev_dir)]
    all_imgs = all_headers + all_prevs

    not_needed = [path for path in all_imgs if path not in in_use]
    
    for path in not_needed:
        if path:
            default_storage.delete(path)
