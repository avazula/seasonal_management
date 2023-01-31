from unittest.mock import patch
import nose.tools
from models.language import Language
from models.streamer import Streamer
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


def test_create_passing_case_check_id(mocker):
    mocker.patch("factories.StreamerFactory.sanitize")
    streamer = StreamerFactory.create(
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
    assert streamer.id == PASSING_ID


def test_create_passing_case_check_username(mocker):
    mocker.patch("factories.StreamerFactory.sanitize")
    streamer = StreamerFactory.create(
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
    assert streamer.username == PASSING_USERNAME


def test_create_passing_case_check_discord_handler(mocker):
    mocker.patch("factories.StreamerFactory.sanitize")
    streamer = StreamerFactory.create(
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
    assert streamer.discord_handler == PASSING_DISCORD_HANDLER


def test_create_passing_case_check_youtube_handler(mocker):
    mocker.patch("factories.StreamerFactory.sanitize")
    streamer = StreamerFactory.create(
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
    assert streamer.youtube_handler == PASSING_YOUTUBE_HANDLER


def test_create_passing_case_check_bilibili_handler(mocker):
    mocker.patch("factories.StreamerFactory.sanitize")
    streamer = StreamerFactory.create(
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
    assert streamer.bilibili_handler == PASSING_BILIBILI_HANDLER


def test_create_passing_case_check_team_is_of_type_team(mocker):
    mocker.patch("factories.StreamerFactory.sanitize")
    streamer = StreamerFactory.create(
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
    assert isinstance(streamer.team, Team)


def test_create_passing_case_check_languages_is_of_type_langugae(mocker):
    mocker.patch("factories.StreamerFactory.sanitize")
    streamer = StreamerFactory.create(
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
    assert isinstance(streamer.languages, list)


def test_create_sanitize_returned_youtube_handler_not_string():
    with patch.object(StreamerFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("youtube_handler must be of type str")
            streamer = StreamerFactory.create(
                id=PASSING_ID,
                username=PASSING_USERNAME,
                youtube_handler=420,
                discord_handler=PASSING_USERNAME,
            )
            assert streamer is None


def test_create_sanitize_returned_youtube_handler_out_of_bounds():
    with patch.object(StreamerFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("youtube_handler must be of length 4 < x < 120")
            streamer = StreamerFactory.create(
                id=PASSING_ID,
                username=PASSING_USERNAME,
                youtube_handler="a" * 120,
                discord_handler=PASSING_USERNAME,
            )
            assert streamer is None


def test_create_sanitize_returned_bilibili_handler_not_string():
    with patch.object(StreamerFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("bilibili_handler must be of type str")
            streamer = StreamerFactory.create(
                id=PASSING_ID,
                username=PASSING_USERNAME,
                bilibili_handler=420,
                discord_handler=PASSING_USERNAME,
            )
            assert streamer is None


def test_create_sanitize_returned_bilibili_handler_out_of_bounds():
    with patch.object(StreamerFactory, "sanitize") as get_mock:
        with nose.tools.assert_raises(Exception):
            get_mock.side_effect = Exception("bilibili_handler must be of length 4 < x < 120")
            streamer = StreamerFactory.create(
                id=PASSING_ID,
                username=PASSING_USERNAME,
                bilibili_handler="a" * 120,
                discord_handler=PASSING_USERNAME,
            )
            assert streamer is None
