from typing import List

from dto import StationDto
from models import Station


# TODO попробуй закончить
class StationService:
    @staticmethod
    def get_all() -> List[StationDto]:
        return [StationDto(**s) for s in Station.query.all()]

    @staticmethod
    def get_one_by_id(id: int) -> StationDto:
        return StationDto(**Station.query.get(id))
