from unittest.mock import patch
import nose.tools
from models.language import Language
from factories.team_factory import TeamFactory


PASSING_ID = 1
PASSING_SHORT_NAME = "WTH"
PASSING_FULL_NAME = "Wolves of War"
PASSING_LANGUAGE = "English"


def test_create_passing_case_check_id(mocker):
    mocker.patch("factories.TeamFactory.sanitize")
    team = TeamFactory.create(
        id=PASSING_ID,
        short_name=PASSING_SHORT_NAME,
        full_name=PASSING_FULL_NAME,
        language=Language(id=PASSING_ID,language=PASSING_LANGUAGE)
    )
    assert team.id == PASSING_ID


def test_create_passing_case_check_short_name(mocker):
    mocker.patch("factories.TeamFactory.sanitize")
    team = TeamFactory.create(
        id=PASSING_ID,
        short_name=PASSING_SHORT_NAME,
        full_name=PASSING_FULL_NAME,
        language=Language(id=PASSING_ID,language=PASSING_LANGUAGE)
    )
    assert team.short_name == PASSING_SHORT_NAME

def test_create_passing_case_check_full_name(mocker):
    mocker.patch("factories.TeamFactory.sanitize")
    team = TeamFactory.create(
        id=PASSING_ID,
        short_name=PASSING_SHORT_NAME,
        full_name=PASSING_FULL_NAME,
        language=Language(id=PASSING_ID,language=PASSING_LANGUAGE)
    )
    assert team.full_name == PASSING_FULL_NAME

def test_create_passing_case_check_language_is_of_type_language(mocker):
    mocker.patch("factories.TeamFactory.sanitize")
    team = TeamFactory.create(
        id=PASSING_ID,
        short_name=PASSING_SHORT_NAME,
        full_name=PASSING_FULL_NAME,
        language=Language(id=PASSING_ID,language=PASSING_LANGUAGE)
    )
    assert isinstance(team.language, Language)




def test_create_sanitize_returned_id_not_integer():
    with patch.object(TeamFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("id must be an integer")
            team = TeamFactory.create(
                id="1",
                short_name=PASSING_SHORT_NAME,
                full_name=PASSING_FULL_NAME,
                language=Language(id=PASSING_ID,language=PASSING_LANGUAGE)
            )
            assert team is None


def test_create_sanitize_returned_id_out_of_bounds():
    with patch.object(TeamFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("id must be greater than 0")
            team = TeamFactory.create(
                id=-1,
                short_name=PASSING_SHORT_NAME,
                full_name=PASSING_FULL_NAME,
                language=Language(id=PASSING_ID,language=PASSING_LANGUAGE)
            )
            assert team is None


def test_create_sanitize_returned_short_name_not_string():
    with patch.object(TeamFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("short_name must be of type str")
            team = TeamFactory.create(
                id=PASSING_ID,
                short_name=420,
                full_name=PASSING_FULL_NAME,
                language=Language(id=PASSING_ID,language=PASSING_LANGUAGE)
            )
            assert team is None


def test_create_sanitize_returned_short_name_out_of_bounds():
    with patch.object(TeamFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("short_name must be of length 2 < x < 15")
            team = TeamFactory.create(
                id=PASSING_ID,
                short_name="a" * 16,
                full_name=PASSING_FULL_NAME,
                language=Language(id=PASSING_ID,language=PASSING_LANGUAGE)
            )
            assert team is None


def test_create_sanitize_returned_full_name_not_string():
    with patch.object(TeamFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("full_name must be of type str")
            team = TeamFactory.create(
                id=PASSING_ID,
                short_name=PASSING_SHORT_NAME,
                full_name=420,
                language=Language(id=PASSING_ID,language=PASSING_LANGUAGE)
            )
            assert team is None


def test_create_sanitize_returned_full_name_out_of_bounds():
    with patch.object(TeamFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("full_name must be of length 6 < x < 120")
            team = TeamFactory.create(
                id=PASSING_ID,
                short_name=PASSING_SHORT_NAME,
                full_name="a" * 120,
                language=Language(id=PASSING_ID,language=PASSING_LANGUAGE)
            )
            assert team is None
