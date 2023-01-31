import pytest
from factories.stage_factory import StageFactory


PASSING_ID = 1
PASSING_NAME = "Playoffs"


def test_stage_factory_sanitize_passing_case():
    invalid_parameters = StageFactory.sanitize(id=PASSING_ID, name=PASSING_NAME)
    assert invalid_parameters is None


def test_stage_factory_sanitize_id_is_not_within_bounds():
    with pytest.raises(Exception) as e_info:
        StageFactory.sanitize(id=-1, name=PASSING_NAME)
        assert e_info == "id must be greater than 0"


def test_stage_factory_sanitize_id_is_string():
    with pytest.raises(Exception) as e_info:
        StageFactory.sanitize(id="1", name=PASSING_NAME)
        assert e_info == "id must be an integer"


def test_stage_factory_sanitize_id_is_float():
    with pytest.raises(Exception) as e_info:
        StageFactory.sanitize(id=1.0, name=PASSING_NAME)
        assert e_info == "id must be an integer"


def test_stage_factory_sanitize_name_is_integer():
    with pytest.raises(Exception) as e_info:
        StageFactory.sanitize(id=PASSING_NAME, name=420)
        assert e_info == "name must be of type str"


def test_stage_factory_sanitize_name_is_out_of_bounds():
    with pytest.raises(Exception) as e_info:
        StageFactory.sanitize(id=PASSING_NAME, name="a" * 41)
        assert e_info == "name must be of length 0 < x < 40"
