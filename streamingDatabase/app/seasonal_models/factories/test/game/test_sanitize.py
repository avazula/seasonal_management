import arrow
import pytest
from models.game import Game
from factories.game_factory import GameFactory

def test_game_factory_sanitize_passing_case():
    invalid_parameters = GameFactory.sanitize(id=1,datetime=arrow.get("2022-05-19 18:00:00"))
    assert invalid_parameters is None

def test_game_factory_sanitize_id_is_not_within_bounds():
    with pytest.raises(Exception) as e_info:
        GameFactory.sanitize(id=-1,datetime=arrow.get("2022-05-19 18:00:00"))
        assert e_info == "id must be greater than 0"

def test_game_factory_sanitize_id_is_string():
    with pytest.raises(Exception) as e_info:
        GameFactory.sanitize(id="1",datetime=arrow.get("2022-05-19 18:00:00"))
        assert e_info == "id must be an integer"

def test_game_factory_sanitize_id_is_float():
    with pytest.raises(Exception) as e_info:
        GameFactory.sanitize(id=1.0,datetime=arrow.get("2022-05-19 18:00:00"))
        assert e_info == "id must be an integer"

def test_game_factory_sanitize_id_is_arrow():
    with pytest.raises(Exception) as e_info:
        GameFactory.sanitize(id=arrow.get(),datetime=arrow.get("2022-05-19 18:00:00"))
        assert e_info == "id must be an integer"

def test_game_factory_sanitize_datetime_is_string():
    with pytest.raises(Exception) as e_info:
        GameFactory.sanitize(id=1,datetime="2022-05-19 18:00:00")
        assert e_info == "datetime must be of type arrow"

def test_game_factory_sanitize_datetime_is_integer():
    with pytest.raises(Exception) as e_info:
        GameFactory.sanitize(id=1,datetime=420)
        assert e_info == "datetime must be of type arrow"

def test_game_factory_sanitize_datetime_is_float():
    with pytest.raises(Exception) as e_info:
        GameFactory.sanitize(id=1,datetime=42.0)
        assert e_info == "datetime must be of type arrow"

def test_game_factory_sanitize_datetime_is_too_old():
    with pytest.raises(Exception) as e_info:
        GameFactory.sanitize(id=1,datetime="2021-05-19 18:00:00")
        assert e_info == "datetime must be more recent than January 1st, 2022 and less than January 1st, 2030"

def test_game_factory_sanitize_datetime_is_too_far_back_in_the_future():
    with pytest.raises(Exception) as e_info:
        GameFactory.sanitize(id=1,datetime="2031-05-19 18:00:00")
        assert e_info == "datetime must be more recent than January 1st, 2022 and less than January 1st, 2030"