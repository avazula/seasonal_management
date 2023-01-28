import arrow
import pytest
from models.game import Game
from factory.game_factory import GameFactory


def test_game_factory_passing_case(mocker):
    mocker.patch("models.game.Game", return_value=Game(id=1,date=arrow.get('2022-05-19 18:00:00')))
    assert GameFactory() == Game(id=1, date=arrow.get('2022-05-19 18:00:00'))
