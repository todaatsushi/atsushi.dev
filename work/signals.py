from django.db.models.signals import post_save
from django.dispatch import receiver

from work.models import Project, ProjectSpecs


# when post_save was called
@receiver(post_save, sender=Project)
def create_project_specs(sender, instance, created, **kwargs):
    if created:
        ProjectSpecs.objects.create(project=instance)


# Save new profile after creation
@receiver(post_save, sender=Project)
def save_project_specs(sender, instance, **kwargs):
    instance.specs.save()
