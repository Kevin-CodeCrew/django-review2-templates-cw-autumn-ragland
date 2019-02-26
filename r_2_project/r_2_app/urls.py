from django.urls import path
from . import views

urlpatterns = [
    path('songs/', views.list_songs, name='list_songs'),
    path('songs/<int:song_id>/', views.list_song, name='song_details'),
]

