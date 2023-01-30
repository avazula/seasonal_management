from unittest.mock import patch
import arrow
import nose.tools
from models.game import Game
from factories.game_factory import GameFactory


def test_create_passing_case_check_id(mocker):
    mocker.patch("factories.GameFactory.sanitize")
    game = GameFactory.create(id=1, datetime=arrow.get("2022-05-19 18:00:00"))
    assert game.id == 1


def test_create_passing_case_check_datetime(mocker):
    mocker.patch("factories.GameFactory.sanitize")
    game = GameFactory.create(id=1, datetime=arrow.get("2022-05-19 18:00:00"))
    assert game.datetime == arrow.get("2022-05-19 18:00:00")


def test_create_sanitize_returned_id_not_integer():
    with patch.object(GameFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("id must be an integer")
            game = GameFactory.create(id="1.0", datetime=arrow.get("2022-05-19 18:00:00"))
            assert game is None


def test_create_sanitize_returned_id_out_of_bounds():
    with patch.object(GameFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("id must be greater than 0")
            game = GameFactory.create(id=-1, datetime=arrow.get("2022-05-19 18:00:00"))
            assert game is None


def test_create_sanitize_returned_datetime_not_arrow():
    with patch.object(GameFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("datetime must be of type arrow")
            game = GameFactory.create(id=1, datetime="2022-05-19 18:00:00")
            assert game is None


def test_create_sanitize_returned_datetime_out_of_bounds():
    with patch.object(GameFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception(
                "datetime must be more recent than January 1st, 2022 and less than January 1st, 2030"
            )
            game = GameFactory.create(id=1, datetime="2031-05-19 18:00:00")
            assert game is None
