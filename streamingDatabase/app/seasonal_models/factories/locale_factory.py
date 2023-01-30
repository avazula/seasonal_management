from models.locale import Locale
from typing import Optional, List


class LocaleFactory:
    @staticmethod
    def sanitize(id: int, time: str, abbreviation: str = None) -> Optional[List[str]]:
        invalid_parameters: List[str] = []
        if id is not None:
            if not isinstance(id, int):
                invalid_parameters.append("id")
                raise Exception("id must be an integer")
            elif id < 1:
                invalid_parameters.append("id")
                raise Exception("id must be greater than 0")
        # time 6
        if time is not None:
            if not isinstance(time, str):
                invalid_parameters.append("time")
                raise Exception("time must be of type str")
            elif len(time) < 3 or len(time) > 6:
                invalid_parameters.append("time")
                raise Exception("time must be of length 0 < x < 6")
        # abbreviation 20
        if abbreviation is not None:
            if not isinstance(abbreviation, str):
                invalid_parameters.append("abbreviation")
                raise Exception("abbreviation must be of type str")
            elif len(abbreviation) < 2 or len(abbreviation) > 20:
                invalid_parameters.append("abbreviation")
                raise Exception("abbreviation must be of length 2 < x < 20")
        return invalid_parameters if invalid_parameters else None

    @staticmethod
    def create(id: int, time: str, abbreviation: str) -> Locale:
        try:
            LocaleFactory.sanitize(id, time, abbreviation)
        except:
            raise
        return Locale(id=id, time=time, abbreviation=abbreviation)
