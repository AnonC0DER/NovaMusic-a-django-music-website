from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from artist.models import Artist


@receiver(pre_save, sender=Artist)
def slugify_pre_save(sender, instance, *args, **kwargs):
    '''Set slug using pre_save signal'''
    title = instance.title
    slug = instance.slug

    if slug is None:
        instance.slug = slugify(title)