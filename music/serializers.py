from rest_framework import serializers
from .models import *


class ArtistSerializers(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class ArtistValidatedSerializer(serializers.Serializer):
    artist_name = serializers.CharField(max_length=77)


class AlbumSerializers(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class AlbumValidateSerializ(serializers.Serializer):
    album_title = serializers.CharField(max_length=40)
    cover = serializers.FileField()
    artist = serializers.IntegerField(min_value=1)
    release_year = serializers.IntegerField(min_value=1980, max_value=2023)


class SongSerializers(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class SongValidateSerializer(serializers.Serializer):
    artist = serializers.IntegerField(min_value=1)
    album = serializers.IntegerField(min_value=1)
    audio_file = serializers.FileField()
    song_title = serializers.CharField(max_length=50)
