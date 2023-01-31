from .language import Language
from typing import Optional


class Team:
    def __init__(
        self,
        id: int,
        short_name: str,
        language: Language,
        full_name: str = None,
    ):
        self._id = id
        self._short_name = short_name
        self._full_name = full_name
        self._language = language

    @property
    def id(self) -> int:
        return self._id

    @property
    def short_name(self) -> str:
        return self._short_name

    @property
    def language(self) -> Language:
        return self._language

    @property
    def full_name(self) -> Optional[str]:
        return self._full_name

    @language.setter
    def language(self, language: Language) -> None:
        self._language = language
