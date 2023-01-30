from models.language import Language
from typing import List, Optional


class LanguageFactory:
    @staticmethod
    def sanitize(id: int, language: str) -> Optional[List[str]]:
        invalid_parameters: List[str] = []
        if id is not None:
            if not isinstance(id, int):
                invalid_parameters.append("id")
                raise Exception("id must be an integer")
            elif id < 1:
                invalid_parameters.append("id")
                raise Exception("id must be greater than 0")
        if language is not None:
            if not isinstance(language, str):
                invalid_parameters.append("language")
                raise Exception("language must be of type str")
            elif len(language) < 3 or len(language) > 50:
                invalid_parameters.append("language")
                raise Exception("language must be of length 3 < x < 50")
        return invalid_parameters if invalid_parameters else None

    @staticmethod
    def create(id: int, language: str) -> Language:
        try:
            LanguageFactory.sanitize(id, language)
        except:
            raise
        return Language(id=id, language=language)
