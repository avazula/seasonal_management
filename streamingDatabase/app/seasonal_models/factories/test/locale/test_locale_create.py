from unittest.mock import patch
import nose.tools
from models.locale import Locale
from factories.locale_factory import LocaleFactory


def test_create_passing_case_check_id(mocker):
    mocker.patch("factories.LocaleFactory.sanitize")
    locale = LocaleFactory.create(id=1, time="UTC+2", abbreviation="CEST")
    assert locale.id == 1


def test_create_passing_case_check_time(mocker):
    mocker.patch("factories.LocaleFactory.sanitize")
    locale = LocaleFactory.create(id=1, time="UTC+2", abbreviation="CEST")
    assert locale.time == "UTC+2"


def test_create_passing_case_check_abbreviation(mocker):
    mocker.patch("factories.LocaleFactory.sanitize")
    locale = LocaleFactory.create(id=1, time="UTC+2", abbreviation="CEST")
    assert locale.abbreviation == "CEST"


def test_create_sanitize_returned_id_not_integer():
    with patch.object(LocaleFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("id must be an integer")
            locale = LocaleFactory.create(id="1.0", time="UTC+2", abbreviation="CEST")
            assert locale is None


def test_create_sanitize_returned_id_out_of_bounds():
    with patch.object(LocaleFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("id must be greater than 0")
            locale = LocaleFactory.create(id=-1, time="UTC+2", abbreviation="CEST")
            assert locale is None


def test_create_sanitize_returned_time_not_string():
    with patch.object(LocaleFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("time must be of type string ")
            locale = LocaleFactory.create(id=1, time=420)
            assert locale is None


def test_create_sanitize_returned_time_out_of_bounds():
    with patch.object(LocaleFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("time must be of length 0 < x < 6")
            locale = LocaleFactory.create(id=1, time="blblblblbl")
            assert locale is None


def test_create_sanitize_returned_abbreviation_not_string():
    with patch.object(LocaleFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("abbreviation must be of type str")
            locale = LocaleFactory.create(id=1, time="UTC+2")
            assert locale is None


def test_create_sanitize_returned_time_out_of_bounds():
    with patch.object(LocaleFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("abbreviation must be of length 2 < x < 20")
            locale = LocaleFactory.create(id=1, time="UTC+2", abbreviation="blblblblblblblblblblblblbl")
            assert locale is None
