from typing import Dict, List

from django.apps import apps
from rest_framework import serializers

from games.models import Game


class GameSerializer(serializers.ModelSerializer):
    """
    Game Serializer.
    Used for update and detail.
    """

    class Meta:
        model = Game
        fields = [
            'id',
            'created_time', 'last_update_time', 'finished_time',
            'secret', 'status',
            'rows', 'cols', 'mines',
            'field_board',
            # Editable fields
            'name', 'game_board',
        ]
        read_only_fields = [
            'id',
            'created_time', 'last_update_time', 'finished_time',
            'secret', 'status',
            'rows', 'cols', 'mines',
            'field_board',
        ]
        extra_kwargs = {
            'name': {'required': False},
            'game_board': {'required': False},
        }


class GameListSerializer(serializers.ModelSerializer):
    """
    Game Serializer.
    Used for lists.
    """

    class Meta:
        model = Game
        fields = [
            'id',
            'created_time', 'last_update_time', 'finished_time',
            'secret', 'status',
            'name',
        ]
        read_only_fields = [
            'id',
            'created_time', 'last_update_time', 'finished_time',
            'secret', 'status',
            'name',
        ]
        extra_kwargs = {
        }
