from unittest.mock import patch
import nose.tools
from models.language import Language
from factories.language_factory import LanguageFactory


def test_create_passing_case_check_id(mocker):
    mocker.patch("factories.LanguageFactory.sanitize")
    language = LanguageFactory.create(id=1, language="Korean")
    assert language.id == 1


def test_create_passing_case_check_datetime(mocker):
    mocker.patch("factories.LanguageFactory.sanitize")
    language = LanguageFactory.create(id=1, language="Korean")
    assert language.language == "Korean"


def test_create_sanitize_returned_id_not_integer():
    with patch.object(LanguageFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("id must be an integer")
            language = LanguageFactory.create(id="1.0", language="Korean")
            assert language is None


def test_create_sanitize_returned_id_out_of_bounds():
    with patch.object(LanguageFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("id must be greater than 0")
            language = LanguageFactory.create(id=-1, language="Korean")
            assert language is None


def test_create_sanitize_returned_language_is_not_string():
    with patch.object(LanguageFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("language must be of type str")
            language = LanguageFactory.create(id=1, language="Korean")
            assert language is None


def test_create_sanitize_returned_language_out_of_bounds():
    with patch.object(LanguageFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("language must be of length 3 < x < 50")
            language = LanguageFactory.create(id=1, language="Koreannnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
            assert language is None
