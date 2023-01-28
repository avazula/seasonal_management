class Language:
    def __init__(self, id: int, language: str):
        self._id = id
        self._language = language

    @property
    def id(self) -> id:
        return self._id

    @property
    def language(self) -> str:
        return self._language
