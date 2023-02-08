from django.urls import path, include
from .views import *
from rest_framework.routers import *

album_router = DefaultRouter()
album_router.register(r'album', AlbumModelViewSet)

artist_router = DefaultRouter()
artist_router.register(r'artist', ArtistModelViewSet)

song_router = DefaultRouter()
song_router.register(r'song', SongModelViewSet)


urlpatterns = (
    path('', include(album_router.urls)),
    # path('album/',
    #      AlbumModelViewSet.as_view({'get': 'list',
    #                                 'post': 'create'})),
    # path('album/<int:pk>/',
    #      AlbumModelViewSet.as_view({'get': 'retrieve',
    #                                 'delete': 'destroy',
    #                                 'put': 'update'})),
    # # path('album/<int:pk>/',
    # #      AlbumModelViewSet.as_view({'get': 'get_all_song'})),
    # path('song/',
    #      SongModelViewSet.as_view({'get': 'list',
    #                                'post': 'create'})),
    # path('song/<int:pk>/'),
    path('', include(artist_router.urls)),
    path('', include(song_router.urls)),
)
