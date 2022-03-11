from django.utils.text import slugify
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from music.models import Music


@receiver(pre_save, sender=Music)
def slugify_pre_save(sender, instance, *args, **kwargs):
    '''Set slug using pre_save signal'''
    title = instance.title
    slug = instance.slug

    if slug is None:
        instance.slug = slugify(title)


@receiver(pre_delete, sender=Music)
def delete_image_pre_delete(sender, instance, *args, **kwargs):
    '''Delete album image when the album object is no longer in database'''
    if instance.thumbnail and instance.thumbnail.url:
        if instance.thumbnail != 'SongsThumbnails/default.jpg':
            instance.thumbnail.delete()