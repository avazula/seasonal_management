from unittest.mock import patch
import nose.tools
from models.language import Language
from models.person import Person
from models.team import Team
from factories.person_factory import PersonFactory

PASSING_ID = 1
PASSING_USERNAME = "avazula"
PASSING_DISCORD_HANDLER = "avazula#2077"
PASSING_LANGUAGE = "English"
PASSING_TEAM_SHORT_NAME = "WTH"
PASSING_TEAM_FULL_NAME = "Wolves of War"


def test_create_passing_case_check_id(mocker):
    mocker.patch("factories.PersonFactory.sanitize")
    person = PersonFactory.create(
        id=PASSING_ID,
        username=PASSING_USERNAME,
        discord_handler=PASSING_DISCORD_HANDLER,
        team=Team(
            id=1,
            short_name=PASSING_TEAM_SHORT_NAME,
            full_name=PASSING_TEAM_FULL_NAME,
            language=Language(id=PASSING_ID, language=PASSING_LANGUAGE),
        ),
    )
    assert person.id == PASSING_ID


def test_create_passing_case_check_username(mocker):
    mocker.patch("factories.PersonFactory.sanitize")
    person = PersonFactory.create(
        id=PASSING_ID,
        username=PASSING_USERNAME,
        discord_handler=PASSING_DISCORD_HANDLER,
        team=Team(
            id=1,
            short_name=PASSING_TEAM_SHORT_NAME,
            full_name=PASSING_TEAM_FULL_NAME,
            language=Language(id=PASSING_ID, language=PASSING_LANGUAGE),
        ),
    )
    assert person.username == PASSING_USERNAME


def test_create_passing_case_check_discord_handler(mocker):
    mocker.patch("factories.PersonFactory.sanitize")
    person = PersonFactory.create(
        id=PASSING_ID,
        username=PASSING_USERNAME,
        discord_handler=PASSING_DISCORD_HANDLER,
        team=Team(
            id=1,
            short_name=PASSING_TEAM_SHORT_NAME,
            full_name=PASSING_TEAM_FULL_NAME,
            language=Language(id=PASSING_ID, language=PASSING_LANGUAGE),
        ),
    )
    assert person.discord_handler == PASSING_DISCORD_HANDLER


def test_create_passing_case_check_team_is_of_type_team(mocker):
    mocker.patch("factories.PersonFactory.sanitize")
    person = PersonFactory.create(
        id=PASSING_ID,
        username=PASSING_USERNAME,
        discord_handler=PASSING_DISCORD_HANDLER,
        team=Team(
            id=1,
            short_name=PASSING_TEAM_SHORT_NAME,
            full_name=PASSING_TEAM_FULL_NAME,
            language=Language(id=PASSING_ID, language=PASSING_LANGUAGE),
        ),
    )
    assert isinstance(person.team, Team)


def test_create_sanitize_returned_id_not_integer():
    with patch.object(PersonFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("id must be an integer")
            person = (
                PersonFactory.create(
                    id="1.0",
                    username=PASSING_USERNAME,
                    discord_handler=PASSING_DISCORD_HANDLER,
                    team=Team(
                        id=1,
                        short_name=PASSING_TEAM_SHORT_NAME,
                        full_name=PASSING_TEAM_FULL_NAME,
                        language=Language(id=PASSING_ID, language=PASSING_LANGUAGE),
                    ),
                ),
            )
            assert person is None


def test_create_sanitize_returned_id_out_of_bounds():
    with patch.object(PersonFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("id must be greater than 0")
            person = (
                PersonFactory.create(
                    id=-1,
                    username=PASSING_USERNAME,
                    discord_handler=PASSING_DISCORD_HANDLER,
                    team=Team(
                        id=1,
                        short_name=PASSING_TEAM_SHORT_NAME,
                        full_name=PASSING_TEAM_FULL_NAME,
                        language=Language(id=PASSING_ID, language=PASSING_LANGUAGE),
                    ),
                ),
            )
            assert person is None


def test_create_sanitize_returned_username_not_string():
    with patch.object(PersonFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("username must be of type str")
            person = (
                PersonFactory.create(
                    id=PASSING_ID,
                    username=420,
                    discord_handler=PASSING_DISCORD_HANDLER,
                    team=Team(
                        id=1,
                        short_name=PASSING_TEAM_SHORT_NAME,
                        full_name=PASSING_TEAM_FULL_NAME,
                        language=Language(id=PASSING_ID, language=PASSING_LANGUAGE),
                    ),
                ),
            )
            assert person is None


def test_create_sanitize_returned_username_out_of_bounds():
    with patch.object(PersonFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("username must be of length 4 < x < 80")
            person = (
                PersonFactory.create(
                    id=PASSING_ID,
                    username="a" * 80,
                    discord_handler=PASSING_DISCORD_HANDLER,
                    team=Team(
                        id=1,
                        short_name=PASSING_TEAM_SHORT_NAME,
                        full_name=PASSING_TEAM_FULL_NAME,
                        language=Language(id=PASSING_ID, language=PASSING_LANGUAGE),
                    ),
                ),
            )
            assert person is None


def test_create_sanitize_returned_discord_handler_not_string():
    with patch.object(PersonFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("discord_handler must be of type str")
            person = (
                PersonFactory.create(
                    id=PASSING_ID,
                    username=PASSING_USERNAME,
                    discord_handler=420,
                    team=Team(
                        id=1,
                        short_name=PASSING_TEAM_SHORT_NAME,
                        full_name=PASSING_TEAM_FULL_NAME,
                        language=Language(id=PASSING_ID, language=PASSING_LANGUAGE),
                    ),
                ),
            )
            assert person is None


def test_create_sanitize_returned_discord_handler_out_of_bounds():
    with patch.object(PersonFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("discord_handler must be of length 7 < x < 120")
            person = (
                PersonFactory.create(
                    id=PASSING_ID,
                    username=PASSING_USERNAME,
                    discord_handler="a" * 121,
                    team=Team(
                        id=1,
                        short_name=PASSING_TEAM_SHORT_NAME,
                        full_name=PASSING_TEAM_FULL_NAME,
                        language=Language(id=PASSING_ID, language=PASSING_LANGUAGE),
                    ),
                ),
            )
            assert person is None
