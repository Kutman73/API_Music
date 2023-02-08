from django.db import models
from django.core.validators import FileExtensionValidator
from .service import *


class Artist(models.Model):
    artist_name = models.CharField(
        max_length=77,
        unique=True
    )

    def __str__(self):
        return self.artist_name


class Album(models.Model):
    album_title = models.CharField(max_length=40)
    cover = models.ImageField(
        blank=True,
        null=True,
        storage=OverWriteStorage(),
        upload_to=FilePath.get_path_to_album_cover,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['png', 'jpg']
            ), FileCheck.check_file_size
        ]
    )
    artist = models.ForeignKey(Artist,
                               on_delete=models.CASCADE,
                               related_name='album')
    release_year = models.PositiveIntegerField()
    creation_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.artist}_{self.album_title}'


class Song(models.Model):
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    audio_file = models.FileField(
        storage=OverWriteStorage(),
        upload_to=FilePath.get_path_to_audio_file,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['mp3']
            )
        ]
    )
    song_title = models.CharField(max_length=50)
    number = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.song_title
