from django.contrib import admin
from django.urls import path
from musicplayer.views import GetAllSongs
urlpatterns = [
    path('admin/',admin.site.urls),
    path('songs/',GetAllSongs.as_view())
]