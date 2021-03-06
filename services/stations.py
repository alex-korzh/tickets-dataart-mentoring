from typing import List
from dto import StationDto, StationListResponse
from models import Station


# TODO попробуй закончить
class StationService:
    @staticmethod
    def get_all() -> StationListResponse:
        stations = Station.query.all()
        return StationListResponse(stations=[StationDto(**s.to_dict()) for s in stations])

    @staticmethod
    def get_one_by_id(id: int) -> StationDto:
        rez_station = Station.query.get(id)
        return StationDto(**rez_station.to_dict())

    @staticmethod
    def get_all_by_locality(id: int) -> StationListResponse:
        stations = Station.query.filter_by(id_locality=id).all()
        return StationListResponse(stations=[StationDto(**s.to_dict()) for s in stations])

    @staticmethod
    def delete_by_id(id: int) -> None:
        rez_station = Station.query.get(id)
        rez_station.delete()
