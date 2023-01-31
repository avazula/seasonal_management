import pytest
from models.language import Language
from factories.team_factory import TeamFactory

PASSING_ID = 1
PASSING_SHORT_NAME = "WTH"
PASSING_FULL_NAME = "Wolves of War"
PASSING_LANGUAGE = "English"


def test_team_factory_sanitize_passing_case():
    invalid_parameters = TeamFactory.sanitize(
        id=PASSING_ID,
        short_name=PASSING_SHORT_NAME,
        full_name=PASSING_FULL_NAME,
        language=Language(id=PASSING_ID, language=PASSING_LANGUAGE),
    )
    assert invalid_parameters is None


def test_team_factory_sanitize_id_is_not_within_bounds():
    with pytest.raises(Exception) as e_info:
        TeamFactory.sanitize(
            id=-1,
            short_name=PASSING_SHORT_NAME,
            full_name=PASSING_FULL_NAME,
            language=Language(id=PASSING_ID, language=PASSING_LANGUAGE),
        )
        assert e_info == "id must be greater than 0"


def test_team_factory_sanitize_id_is_string():
    with pytest.raises(Exception) as e_info:
        TeamFactory.sanitize(
            id="1",
            short_name=PASSING_SHORT_NAME,
            full_name=PASSING_FULL_NAME,
            language=Language(id=PASSING_ID, language=PASSING_LANGUAGE),
        )
        assert e_info == "id must be an integer"


def test_team_factory_sanitize_id_is_float():
    with pytest.raises(Exception) as e_info:
        TeamFactory.sanitize(
            id=1.0,
            short_name=PASSING_SHORT_NAME,
            full_name=PASSING_FULL_NAME,
            language=Language(id=PASSING_ID, language=PASSING_LANGUAGE),
        )
        assert e_info == "id must be an integer"


def test_team_factory_sanitize_short_name_is_integer():
    with pytest.raises(Exception) as e_info:
        TeamFactory.sanitize(
            id=1.0,
            short_name=420,
            full_name=PASSING_FULL_NAME,
            language=Language(id=PASSING_ID, language=PASSING_LANGUAGE),
        )
        assert e_info == "short_name must be of type str"


def test_team_factory_sanitize_short_name_is_out_of_bounds():
    with pytest.raises(Exception) as e_info:
        TeamFactory.sanitize(
            id=1.0,
            short_name="a" * 16,
            full_name=PASSING_FULL_NAME,
            language=Language(id=PASSING_ID, language=PASSING_LANGUAGE),
        )
        assert e_info == "short_name must be of length 2 < x < 15"


def test_team_factory_sanitize_full_name_is_integer():
    with pytest.raises(Exception) as e_info:
        TeamFactory.sanitize(
            id=1.0,
            short_name=PASSING_SHORT_NAME,
            full_name=420,
            language=Language(id=PASSING_ID, language=PASSING_LANGUAGE),
        )
        assert e_info == "full_name must be of type str"


def test_team_factory_sanitize_full_name_is_out_of_bounds():
    with pytest.raises(Exception) as e_info:
        TeamFactory.sanitize(
            id=1.0,
            short_name=PASSING_SHORT_NAME,
            full_name="a" * 121,
            language=Language(id=PASSING_ID, language=PASSING_LANGUAGE),
        )
        assert e_info == "full_name must be of length 6 < x < 121"


def test_team_factory_sanitize_language_is_not_of_type_language():
    with pytest.raises(Exception) as e_info:
        TeamFactory.sanitize(
            id=1.0, short_name=PASSING_SHORT_NAME, full_name=PASSING_FULL_NAME, language=PASSING_LANGUAGE
        )
        assert e_info == "language must be of type Language"
