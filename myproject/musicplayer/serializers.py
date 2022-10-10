from rest_framework import serializers
from .models import MusicPlayer

class GetAllMusicSongSerializer(serializers.ModelSerializer):

    class Meta:
        model = MusicPlayer
        fields = ('name','singer','path','image')