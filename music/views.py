from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import *
from .models import *
from .serializers import *


class ArtistModelViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializers
    lookup_field = 'pk'


class AlbumModelViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializers
    lookup_field = 'pk'


class SongModelViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializers
    lookup_field = 'pk'

    @action(detail=False, methods=['get'])
    def get_all_song(self, request, **kwargs):
        album = self.queryset.filter(
            artist_id=kwargs['songs']
        )
        serializer = self.serializer_class(album, many=True)
        return Response(data=serializer.data)
