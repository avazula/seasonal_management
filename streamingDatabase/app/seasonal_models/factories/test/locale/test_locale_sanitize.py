import pytest
from factories.locale_factory import LocaleFactory


def test_locale_factory_sanitize_passing_case():
    invalid_parameters = LocaleFactory.sanitize(id=1, time="UTC+2", abbreviation="CEST")
    assert invalid_parameters is None


def test_locale_factory_sanitize_id_is_not_within_bounds():
    with pytest.raises(Exception) as e_info:
        LocaleFactory.sanitize(id=-1, time="UTC+2", abbreviation="CEST")
        assert e_info == "id must be greater than 0"


def test_locale_factory_sanitize_id_is_string():
    with pytest.raises(Exception) as e_info:
        LocaleFactory.sanitize(id="1", time="UTC+2", abbreviation="CEST")
        assert e_info == "id must be an integer"


def test_locale_factory_sanitize_id_is_float():
    with pytest.raises(Exception) as e_info:
        LocaleFactory.sanitize(id=1.0, time="UTC+2", abbreviation="CEST")
        assert e_info == "id must be an integer"


def test_locale_factory_sanitize_time_is_out_of_bounds():
    with pytest.raises(Exception) as e_info:
        LocaleFactory.sanitize(id=1, time="UTC+223", abbreviation="CEST")
        assert e_info == "time must be of length 0 < x < 6"


def test_locale_factory_sanitize_time_is_integer():
    with pytest.raises(Exception) as e_info:
        LocaleFactory.sanitize(id=1, time=420, abbreviation="CEST")
        assert e_info == "time must be of type str"


def test_locale_factory_sanitize_abbreviation_is_out_of_bounds():
    with pytest.raises(Exception) as e_info:
        LocaleFactory.sanitize(id=1, time="UTC+2", abbreviation="CESTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
        assert e_info == "time must be of length 0 < x < 6"


def test_locale_factory_sanitize_abbreviation_is_integer():
    with pytest.raises(Exception) as e_info:
        LocaleFactory.sanitize(id=1, time="UTC+2", abbreviation=420)
        assert e_info == "time must be of type str"
