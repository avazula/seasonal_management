from .language import Language


class Team:
    def __init__(self, id: int, short_name: str, full_name: str = None, language: Language = None):
        self._id = id
        self._short_name = short_name
        self._full_name = full_name
        self._language = language
