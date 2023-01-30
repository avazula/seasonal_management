from models.language import Language
from models.streamer import Streamer
from models.team import Team
from typing import Optional, List


class StreamerFactory:
    @staticmethod
    def sanitize(
        id: int,
        username: str,
        discord_handler: str,
        twitch_handler: str = None,
        youtube_handler: str = None,
        bilibili_handler: str = None,
        team: Team = None,
        languages: List[Language] = None,
    ) -> Optional[Streamer]:
        invalid_parameters: List[str] = []
        if id is not None:
            if not isinstance(id, int):
                invalid_parameters.append("id")
                raise Exception("id must be an integer")
            elif id < 1:
                invalid_parameters.append("id")
                raise Exception("id must be greater than 0")
        if username is not None:
            if not isinstance(username, str):
                invalid_parameters.append("username")
                raise Exception("username must be of type str")
            elif len(username) < 4 or len(username) > 80:
                invalid_parameters.append("username")
                raise Exception("time must be of length 4 < x < 80")
        if discord_handler is not None:
            if not isinstance(discord_handler, str):
                invalid_parameters.append("discord_handler")
                raise Exception("discord_handler must be of type str")
            elif len(discord_handler) < 7 or len(discord_handler) > 120:
                invalid_parameters.append("discord_handler")
                raise Exception("time must be of length 7 < x < 120")
        if team is not None:
            if not isinstance(team, Team):
                invalid_parameters.append("team")
                raise Exception("team must be of type Team")
        if youtube_handler is not None:
            if not isinstance(youtube_handler, str):
                invalid_parameters.append("youtube_handler")
                raise Exception("youtube_handler must be of type str")
            elif len(youtube_handler) < 4 or len(youtube_handler) > 120:
                invalid_parameters.append("youtube_handler")
                raise Exception("time must be of length 4 < x < 120")
        if bilibili_handler is not None:
            if not isinstance(bilibili_handler, str):
                invalid_parameters.append("bilibili_handler")
                raise Exception("bilibili_handler must be of type str")
            elif len(bilibili_handler) < 4 or len(bilibili_handler) > 120:
                invalid_parameters.append("bilibili_handler")
                raise Exception("time must be of length 4 < x < 120")
        if twitch_handler is not None:
            if not isinstance(twitch_handler, str):
                invalid_parameters.append("twitch_handler")
                raise Exception("twitch_handler must be of type str")
            elif len(twitch_handler) < 4 or len(twitch_handler) > 120:
                invalid_parameters.append("twitch_handler")
                raise Exception("time must be of length 4 < x < 120")
        if languages is not None:
            if not isinstance(languages, List):
                invalid_parameters.append("languages")
                raise Exception("languages must be of type list")
            else:
                for language in languages:
                    if not isinstance(language, Language):
                        invalid_parameters.append("languages")
                        raise Exception("language must be of type Language")
        return invalid_parameters if invalid_parameters else None

    @staticmethod
    def create(
        id: int,
        username: str,
        discord_handler: str,
        twitch_handler: str,
        youtube_handler: str,
        bilibili_handler: str,
        team: Team,
        languages: List[Language],
    ) -> Optional[Streamer]:
        try:
            StreamerFactory.sanitize(
                id=id,
                username=username,
                discord_handler=discord_handler,
                twitch_handler=twitch_handler,
                youtube_handler=youtube_handler,
                bilibili_handler=bilibili_handler,
                team=team,
                languages=languages,
            )
        except:
            raise
        return Streamer(
            id=id,
            username=username,
            discord_handler=discord_handler,
            twitch_handler=twitch_handler,
            youtube_handler=youtube_handler,
            bilibili_handler=bilibili_handler,
            team=team,
            languages=languages,
        )
