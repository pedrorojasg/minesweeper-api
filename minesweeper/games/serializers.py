import random
from typing import Dict, List, Tuple

from django.apps import apps
from rest_framework import serializers

from games.models import Game

DEFAULT_ROWS = 8
DEFAULT_COLS = 8
DEFAULT_MINES = 10

def get_init_boards(rows: int, cols: int, mines: int) -> Tuple[List, List]:
    field_board: List = []
    game_board: List = []
    length: int = rows*cols
    indexes: List = list(range(0,length))
    mines_index: List = []

    while len(mines_index) < mines:
        index = random.choice(indexes)
        if index not in mines_index:
            mines_index.append(index)

    n: int = 0
    for i in range(0, rows):
        field_row = []
        game_row = []
        for j in range(0, cols):
            if n in mines_index:
                field_row.append('m')
            else:
                field_row.append('')
            game_row.append('')
            n += 1

        field_board.append(field_row)
        game_board.append(game_row)

    return (field_board, game_board)


class GameSerializer(serializers.ModelSerializer):
    """
    Game Serializer.
    Used for create and detail.
    """
    owner = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Game
        fields = [
            'id',
            'owner',
            'created_time', 'last_update_time', 'finished_time',
            'secret', 'status',
            'rows', 'cols', 'mines',
            'field_board', 'game_board',
            # Editable fields
            'name',
        ]
        read_only_fields = [
            'id',
            'created_time', 'last_update_time', 'finished_time',
            'secret', 'status',
            'field_board', 'game_board',
        ]
        extra_kwargs = {
            'name': {'required': False},
            'rows': {'required': False, 'default': DEFAULT_ROWS},
            'cols': {'required': False, 'default': DEFAULT_COLS},
            'mines': {'required': False, 'default': DEFAULT_MINES},
        }

    def validate(self, data):
        if 'cols' in data and 'rows' not in data:
            raise serializers.ValidationError(detail={
                'detail': 'rows field can not be null.'})
        elif 'cols' not in data and 'rows' in data:
            raise serializers.ValidationError(detail={
                'detail': 'cols field can not be null.'})

        size = data['rows']*data['cols']
        mines = data['mines']
        max_mines = 0.5*size
        if mines > max_mines:
            raise serializers.ValidationError(detail={
                'detail': 'Mines should be less than %s' % max_mines})

        return data

    def create(self, validated_data):
        """
        """
        rows = validated_data.get('rows')
        cols = validated_data.get('cols')
        mines = validated_data.get('mines')
        (field_board, game_board) = get_init_boards(rows, cols, mines)
        return Game.objects.create(
                field_board=field_board, game_board=game_board,
                **validated_data)


class GameUpdateSerializer(serializers.ModelSerializer):
    """
    Game Serializer.
    Used for create and detail.
    """

    class Meta:
        model = Game
        fields = [
            # Editable fields
            'name', 'game_board',
        ]
        read_only_fields = [
            'id',
        ]
        extra_kwargs = {
            'name': {'required': False},
            'game_board': {'required': False},
        }


class GameListSerializer(GameSerializer):
    """
    Game Serializer.
    Used for lists.
    """

    class Meta:
        model = Game
        fields = [
            'id',
            'owner',
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
