from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from genre.models import Genre


@receiver(pre_save, sender=Genre)
def slugify_pre_save(sender, instance, *args, **kwargs):
    '''Set slug using pre_save signal'''
    title = instance.title
    slug = instance.slug

    if slug is None:
        instance.slug = slugify(title)