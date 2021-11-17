from typing import List
from dto import StationDto
from models import Station


# TODO попробуй закончить
class StationService:
    @staticmethod
    def get_all() -> List[StationDto]:
        stations = Station.query.all()
        return [StationDto(**s.to_dict()) for s in stations]

    @staticmethod
    def get_one_by_id(id: int) -> StationDto:
        rez_station = Station.query.get(id)
        return StationDto(**rez_station.to_dict())
