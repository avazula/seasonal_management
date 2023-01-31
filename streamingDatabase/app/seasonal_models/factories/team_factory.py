from models.language import Language
from models.team import Team
from typing import Optional, List


class TeamFactory:
    @staticmethod
    def sanitize(id: int, short_name: str, language: Language, full_name: str = None) -> Optional[List[str]]:
        invalid_parameters: List[str] = []
        if id is not None:
            if not isinstance(id, int):
                invalid_parameters.append("id")
                raise Exception("id must be an integer")
            elif id < 1:
                invalid_parameters.append("id")
                raise Exception("id must be greater than 0")
        if short_name is not None:
            if not isinstance(short_name, str):
                invalid_parameters.append("short_name")
                raise Exception("short_name must be of type str")
            elif len(short_name) < 2 or len(short_name) > 15:
                invalid_parameters.append("short_name")
                raise Exception("short_name must be of length 2 < x < 15")
        if language is not None:
            if not isinstance(language, Language):
                invalid_parameters.append("language")
                raise Exception("language must be of type Language")
        if full_name is not None:
            if not isinstance(full_name, str):
                invalid_parameters.append("full_name")
                raise Exception("full_name must be of type str")
            elif len(full_name) < 6 or len(full_name) > 120:
                invalid_parameters.append("full_name")
                raise Exception("full_name must be of length 6 < x < 120")
        return invalid_parameters if invalid_parameters else None

    @staticmethod
    def create(id: int, short_name: str, language: Language, full_name: str) -> Optional[Team]:
        try:
            TeamFactory.sanitize(id=id, short_name=short_name, language=language, full_name=full_name)
        except:
            raise
        return Team(id=id, short_name=short_name, language=language, full_name=full_name)
