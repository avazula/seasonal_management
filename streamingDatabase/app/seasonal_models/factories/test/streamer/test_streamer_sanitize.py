import pytest
from models.language import Language
from models.team import Team
from factories.streamer_factory import StreamerFactory

PASSING_ID = 1
PASSING_USERNAME = "avazula"
PASSING_DISCORD_HANDLER = "avazula#2077"
PASSING_LANGUAGE = "English"
PASSING_TEAM_SHORT_NAME = "WTH"
PASSING_TEAM_FULL_NAME = "Wolves of War"
PASSING_YOUTUBE_HANDLER = "avazula"
PASSING_TWITCH_HANDLER = "avazula"
PASSING_BILIBILI_HANDLER = "12345678"


def test_streamer_factory_sanitize_passing_case():
    invalid_parameters = StreamerFactory.sanitize(
        id=PASSING_ID,
        username=PASSING_USERNAME,
        discord_handler=PASSING_DISCORD_HANDLER,
        team=Team(
            id=1,
            short_name=PASSING_TEAM_SHORT_NAME,
            full_name=PASSING_TEAM_FULL_NAME,
            language=Language(id=PASSING_ID, language=PASSING_LANGUAGE),
        ),
        twitch_handler=PASSING_TWITCH_HANDLER,
        youtube_handler=PASSING_YOUTUBE_HANDLER,
        bilibili_handler=PASSING_BILIBILI_HANDLER,
        languages=[Language(id=PASSING_ID, language=PASSING_LANGUAGE)],
    )
    assert invalid_parameters is None


def test_streamer_factory_sanitize_passing_case_without_optional_parameters():
    invalid_parameters = StreamerFactory.sanitize(
        id=PASSING_ID,
        username=PASSING_USERNAME,
        discord_handler=PASSING_USERNAME,
    )
    assert invalid_parameters is None


def test_streamer_factory_sanitize_id_is_not_within_bounds():
    with pytest.raises(Exception) as e_info:
        StreamerFactory.sanitize(
            id=-1,
            username=PASSING_USERNAME,
            discord_handler=PASSING_USERNAME,
        )
        assert e_info == "id must be greater than 0"


def test_streamer_factory_sanitize_id_is_string():
    with pytest.raises(Exception) as e_info:
        StreamerFactory.sanitize(
            id="1",
            username=PASSING_USERNAME,
            discord_handler=PASSING_USERNAME,
        )
        assert e_info == "id must be an integer"


def test_streamer_factory_sanitize_id_is_float():
    with pytest.raises(Exception) as e_info:
        StreamerFactory.sanitize(
            id=1.0,
            username=PASSING_USERNAME,
            discord_handler=PASSING_USERNAME,
        )
        assert e_info == "id must be an integer"


def test_streamer_factory_sanitize_twitch_handler_is_integer():
    with pytest.raises(Exception) as e_info:
        StreamerFactory.sanitize(
            id=PASSING_ID,
            username=PASSING_USERNAME,
            twitch_handler=420,
            discord_handler=PASSING_USERNAME,
        )
        assert e_info == "twitch_handler must be of type str"


def test_streamer_factory_sanitize_twitch_handler_is_out_of_bounds():
    with pytest.raises(Exception) as e_info:
        StreamerFactory.sanitize(
            id=PASSING_ID,
            username=PASSING_USERNAME,
            twitch_handler="a" * 121,
            discord_handler=PASSING_USERNAME,
        )
        assert e_info == "twitch_handler must be of length 4 < x < 120"


def test_streamer_factory_sanitize_youtube_handler_is_integer():
    with pytest.raises(Exception) as e_info:
        StreamerFactory.sanitize(
            id=PASSING_ID,
            username=PASSING_USERNAME,
            youtube_handler=420,
            discord_handler=PASSING_USERNAME,
        )
        assert e_info == "youtube_handler must be of type str"


def test_streamer_factory_sanitize_youtube_handler_is_out_of_bounds():
    with pytest.raises(Exception) as e_info:
        StreamerFactory.sanitize(
            id=PASSING_ID,
            username=PASSING_USERNAME,
            youtube_handler="a" * 121,
            discord_handler=PASSING_USERNAME,
        )
        assert e_info == "youtube_handler must be of length 4 < x < 120"


def test_streamer_factory_sanitize_bilibili_handler_is_integer():
    with pytest.raises(Exception) as e_info:
        StreamerFactory.sanitize(
            id=PASSING_ID,
            username=PASSING_USERNAME,
            bilibili_handler=420,
            discord_handler=PASSING_USERNAME,
        )
        assert e_info == "bilibili_handler must be of type str"


def test_streamer_factory_sanitize_bilibili_handler_is_out_of_bounds():
    with pytest.raises(Exception) as e_info:
        StreamerFactory.sanitize(
            id=PASSING_ID,
            username=PASSING_USERNAME,
            bilibili_handler="a" * 121,
            discord_handler=PASSING_USERNAME,
        )
        assert e_info == "bilibili_handler must be of length 4 < x < 120"


def test_streamer_factory_sanitize_languages_is_not_list():
    with pytest.raises(Exception) as e_info:
        StreamerFactory.sanitize(
            id=PASSING_ID, username=PASSING_USERNAME, discord_handler=PASSING_USERNAME, languages="English"
        )
        assert e_info == "languages must be of type list"


def test_streamer_factory_sanitize_language_is_not_of_type_language():
    with pytest.raises(Exception) as e_info:
        StreamerFactory.sanitize(
            id=PASSING_ID, username=PASSING_USERNAME, discord_handler=PASSING_USERNAME, languages=["English"]
        )
        assert e_info == "languages must be of type Language"
