import pprint
from typing import Dict, List, Tuple

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.test import APITestCase

from games import utils
from games.models import Game
from games.serializers import GameSerializer


def create_game(**kwargs):
    """
    Create a game with given params.
    """
    serial_data = GameSerializer(data=kwargs)
    if serial_data.is_valid():
        return serial_data.save()
    else:
        return None


def mines_counter(field_board: List) -> int:
    """
    Count mines in a given field_board.
    """
    n: int = 0
    for row in field_board:
        for elem in row:
            if elem == 'm':
                n += 1

    return n


class GameTests(APITestCase):

    def test_create_empty_game(self):
        """
        Ensure we can create a new Game object.
        """
        url = reverse('games:list_create')
        response = self.client.post(url, format='json')
        game = Game.objects.get()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Game.objects.count(), 1)
        self.assertEqual(game.rows, utils.DEFAULT_ROWS)
        self.assertEqual(game.cols, utils.DEFAULT_COLS)
        self.assertEqual(game.mines, utils.DEFAULT_MINES)
        self.assertEqual(game.mines, mines_counter(game.field_board))
        # self.assertEqual(response.data, {"message":"Hello"})
    
    def test_create_custom_game(self):
        """
        Ensure we can create a new Game object with custom params.
        """
        url = reverse('games:list_create')
        data = {'rows': 9, 'cols': 10, 'mines': 12}
        response = self.client.post(url, data, format='json')
        game = Game.objects.get()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Game.objects.count(), 1)
        self.assertEqual(game.rows, 9)
        self.assertEqual(game.cols, 10)
        self.assertEqual(game.mines, 12)
        self.assertEqual(game.mines, mines_counter(game.field_board))
    
    def test_list_games(self):
        """
        Ensure the list returns the correct data.
        """
        url = reverse('games:list_create')
        create_game()
        create_game(rows=10, cols=11)
        response = self.client.get(url, format='json')
        self.assertEqual(Game.objects.all().count(), 2)
        self.assertEqual(len(response.data), 0) # No list data when no user logged
