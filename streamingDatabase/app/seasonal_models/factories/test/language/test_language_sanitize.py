import pytest
from factories.language_factory import LanguageFactory


def test_language_factory_sanitize_passing_case():
    invalid_parameters = LanguageFactory.sanitize(id=1, language="Korean")
    assert invalid_parameters is None


def test_language_factory_sanitize_id_is_not_within_bounds():
    with pytest.raises(Exception) as e_info:
        LanguageFactory.sanitize(id=-1, language="Korean")
        assert e_info == "id must be greater than 0"


def test_language_factory_sanitize_id_is_string():
    with pytest.raises(Exception) as e_info:
        LanguageFactory.sanitize(id="1", language="Korean")
        assert e_info == "id must be an integer"


def test_language_factory_sanitize_id_is_float():
    with pytest.raises(Exception) as e_info:
        LanguageFactory.sanitize(id=1.0, language="Korean")
        assert e_info == "id must be an integer"


def test_language_factory_sanitize_language_is_out_of_bounds():
    with pytest.raises(Exception) as e_info:
        LanguageFactory.sanitize(id=1, language="Koreannnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
        assert e_info == "language must be of length 3 < x < 50"


def test_language_factory_sanitize_language_is_integer():
    with pytest.raises(Exception) as e_info:
        LanguageFactory.sanitize(id=1, language=420)
        assert e_info == "language must be of type str"
