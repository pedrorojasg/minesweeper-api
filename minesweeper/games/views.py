from django.db.models.query import QuerySet
from rest_framework import generics, status
from rest_framework.response import Response

from games.serializers import (
    GameSerializer, GameUpdateSerializer, GameListSerializer
)
from games.models import Game


class GameListCreateView(generics.ListCreateAPIView):
    """
    Game List or Create View.
    """
    serializer_class = GameSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GameListSerializer
        else: # POST
            return GameSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Game.objects.filter(owner=user)
        else:
            return Game.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if user.is_authenticated:
            serializer.save(owner=self.request.user)
        else:
            serializer.save()


class GameRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    """
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GameSerializer
        else: # PUT
            return GameUpdateSerializer
