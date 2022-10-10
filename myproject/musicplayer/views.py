from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MusicPlayer
from .serializers import GetAllMusicSongSerializer
# Create your views here.

class GetAllSongs(APIView):

    def get(self, request):
        listSong = MusicPlayer.objects.all()
        mydata = GetAllMusicSongSerializer(listSong,many=True)
        return Response(data=mydata.data,status=status.HTTP_200_OK)