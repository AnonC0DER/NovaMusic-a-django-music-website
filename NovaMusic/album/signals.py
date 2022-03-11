from django.utils.text import slugify
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from album.models import Album


@receiver(pre_save, sender=Album)
def slugify_pre_save(sender, instance, *args, **kwargs):
    '''Set slug using pre_save signal'''
    title = instance.title
    slug = instance.slug

    if slug is None:
        instance.slug = slugify(title)


@receiver(pre_delete, sender=Album)
def delete_image_pre_delete(sender, instance, *args, **kwargs):
    '''Delete album image when the album object is no longer in database'''
    if instance.album_image and instance.album_image.url:
        if instance.album_image != 'AlbumsImages/default.jpg':
            instance.album_image.delete()