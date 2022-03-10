from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from music.models import Music


@receiver(pre_save, sender=Music)
def slugify_pre_save(sender, instance, *args, **kwargs):
    '''Set slug using pre_save signal'''
    title = instance.title
    slug = instance.slug

    if slug is None:
        instance.slug = slugify(title)