import pytest
from models.language import Language
from models.team import Team
from factories.person_factory import PersonFactory


def test_person_factory_sanitize_passing_case():
    invalid_parameters = PersonFactory.sanitize(
        id=1,
        username="avazula",
        discord_handler="avazula#2077",
        team=Team(id=1, short_name="WTH", full_name="Wolves of War", language=Language(id=1, language="English")),
    )
    assert invalid_parameters is None


def test_person_factory_sanitize_id_is_not_within_bounds():
    with pytest.raises(Exception) as e_info:
        PersonFactory.sanitize(
            id=-1,
            username="avazula",
            discord_handler="avazula#2077",
            team=Team(id=1, short_name="WTH", full_name="Wolves of War", language=Language(id=1, language="English")),
        )
        assert e_info == "id must be greater than 0"


def test_person_factory_sanitize_id_is_string():
    with pytest.raises(Exception) as e_info:
        PersonFactory.sanitize(
            id="1",
            username="avazula",
            discord_handler="avazula#2077",
            team=Team(id=1, short_name="WTH", full_name="Wolves of War", language=Language(id=1, language="English")),
        )
        assert e_info == "id must be an integer"


def test_person_factory_sanitize_id_is_float():
    with pytest.raises(Exception) as e_info:
        PersonFactory.sanitize(
            id=1.0,
            username="avazula",
            discord_handler="avazula#2077",
            team=Team(id=1, short_name="WTH", full_name="Wolves of War", language=Language(id=1, language="English")),
        )
        assert e_info == "id must be an integer"


def test_person_factory_sanitize_username_is_integer():
    with pytest.raises(Exception) as e_info:
        PersonFactory.sanitize(
            id=1,
            username=420,
            discord_handler="avazula#2077",
            team=Team(id=1, short_name="WTH", full_name="Wolves of War", language=Language(id=1, language="English")),
        )
        assert e_info == "username must be of type str"


def test_person_factory_sanitize_username_is_out_of_bounds():
    with pytest.raises(Exception) as e_info:
        PersonFactory.sanitize(
            id=1,
            username="a" * 81,
            discord_handler="avazula#2077",
            team=Team(id=1, short_name="WTH", full_name="Wolves of War", language=Language(id=1, language="English")),
        )
        assert e_info == "username must be of length 0 < x < 80"


def test_person_factory_sanitize_discord_handler_is_integer():
    with pytest.raises(Exception) as e_info:
        PersonFactory.sanitize(
            id=1,
            username="avazula",
            discord_handler=420,
            team=Team(id=1, short_name="WTH", full_name="Wolves of War", language=Language(id=1, language="English")),
        )
        assert e_info == "discord_handler must be of type str"


def test_person_factory_sanitize_discord_handler_is_out_of_bounds():
    with pytest.raises(Exception) as e_info:
        PersonFactory.sanitize(
            id=1,
            username="avazula",
            discord_handler="a" * 121,
            team=Team(id=1, short_name="WTH", full_name="Wolves of War", language=Language(id=1, language="English")),
        )
        assert e_info == "discord_handler must be of length 0 < x < 120"


def test_person_factory_sanitize_team_is_string():
    with pytest.raises(Exception) as e_info:
        PersonFactory.sanitize(id=1, username="avazula", discord_handler="avazula#2077" * 121, team="WTH")
        assert e_info == "team must be of type Team"
