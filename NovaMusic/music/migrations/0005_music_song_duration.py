# Generated by Django 3.2.9 on 2022-03-15 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_rename_genre_music_genres'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='song_duration',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]