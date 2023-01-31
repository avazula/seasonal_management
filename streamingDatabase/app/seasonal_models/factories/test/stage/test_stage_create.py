import nose.tools
from unittest.mock import patch
from factories.stage_factory import StageFactory


PASSING_ID = 1
PASSING_NAME = "Playoffs"


def test_create_passing_case_check_id(mocker):
    mocker.patch("factories.StageFactory.sanitize")
    stage = StageFactory.create(
        id=PASSING_ID,
        name=PASSING_NAME,
    )
    assert stage.id == PASSING_ID


def test_create_passing_case_check_name(mocker):
    mocker.patch("factories.StageFactory.sanitize")
    stage = StageFactory.create(
        id=PASSING_ID,
        name=PASSING_NAME,
    )
    assert stage.name == PASSING_NAME


def test_create_sanitize_returned_id_not_integer():
    with patch.object(StageFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("id must be an integer")
            stage = StageFactory.create(
                id="1",
                name=PASSING_NAME,
            )
            assert stage is None


def test_create_sanitize_returned_id_out_of_bounds():
    with patch.object(StageFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("id must be greater than 0")
            stage = StageFactory.create(
                id=-1,
                name=PASSING_NAME,
            )
            assert stage is None


def test_create_sanitize_returned_name_not_string():
    with patch.object(StageFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("name must be of type str")
            stage = StageFactory.create(
                id=PASSING_ID,
                name=420,
            )
            assert stage is None


def test_create_sanitize_returned_name_out_of_bounds():
    with patch.object(StageFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("name must be of type str")
            stage = StageFactory.create(
                id=PASSING_ID,
                name="a" * 41,
            )
            assert stage is None
