from models.stage import Stage
from typing import Optional, List


class StageFactory:
    @staticmethod
    def sanitize(id, name) -> Optional[List[str]]:
        invalid_parameters: List[str] = []
        if id is not None:
            if not isinstance(id, int):
                invalid_parameters.append("id")
                raise Exception("id must be an integer")
            elif id < 1:
                invalid_parameters.append("id")
                raise Exception("id must be greater than 0")
        if name is not None:
            if not isinstance(name, str):
                invalid_parameters.append("name")
                raise Exception("name must be of type str")
            elif len(name) < 2 or len(name) > 40:
                invalid_parameters.append("name")
                raise Exception("name must be of length 2 < x < 40")
        return invalid_parameters if invalid_parameters else None

    @staticmethod
    def create(id, name) -> Optional[Stage]:
        try:
            StageFactory.sanitize(id, name)
        except:
            raise
        return Stage(id=id, name=name)
