from typing import List
from dto import LocalityDto, LocalityListResponse
from models import Locality


class LocalityService:
    @staticmethod
    def get_all() -> LocalityListResponse:
        localities = Locality.query.all()
        return LocalityListResponse(localities=[LocalityDto(**s.to_dict()) for s in localities])

    @staticmethod
    def get_one_by_id(id: int) -> LocalityDto:
        rez_localities = Locality.query.get(id)
        return LocalityDto(**rez_localities.to_dict())

    @staticmethod
    def delete_by_id(id: int) -> None:
        rez_locality = Locality.query.get(id)
        rez_locality.delete()

    @staticmethod
    def put_by_id(id: int, request) -> None:
        rez_locality = Locality.query.get(id)
        rez_locality.update(request)
