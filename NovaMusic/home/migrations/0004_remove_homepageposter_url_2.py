# Generated by Django 3.2.9 on 2022-03-15 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_url_homepageposter_albums_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepageposter',
            name='url_2',
        ),
    ]
