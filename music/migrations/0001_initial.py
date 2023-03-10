# Generated by Django 4.1.4 on 2023-02-08 16:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import music.service


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_title', models.CharField(max_length=40)),
                ('cover', models.ImageField(blank=True, null=True, storage=music.service.OverWriteStorage(), upload_to=music.service.FilePath.get_path_to_album_cover, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg']), music.service.FileCheck.check_file_size])),
                ('release_year', models.PositiveIntegerField()),
                ('creation_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=77, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_file', models.FileField(storage=music.service.OverWriteStorage(), upload_to=music.service.FilePath.get_path_to_audio_file, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3'])])),
                ('song_title', models.CharField(max_length=50)),
                ('number', models.PositiveIntegerField(default=1)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.artist')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to='music.artist'),
        ),
    ]
