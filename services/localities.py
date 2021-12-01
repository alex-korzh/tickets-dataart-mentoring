from typing import List
from dto import LocalityDto
from models import Locality
from http import HTTPStatus

class LocalityService:
    @staticmethod
    def get_all() -> List[LocalityDto]:
        localities = Locality.query.all()
        return [LocalityDto(**s.to_dict()) for s in localities]

    @staticmethod
    def get_one_by_id(id: int) -> LocalityDto:
        rez_localities = Locality.query.get(id)
        return LocalityDto(**rez_localities.to_dict())

    @staticmethod
    def delete_by_id(id: int) -> LocalityDto:
        rez_locality = Locality.query.get(id)
        rez_locality.delete()

    @staticmethod
    def put_by_id(id: int, request) -> LocalityDto:
        rez_locality = Locality.query.get(id)
        rez_locality.update(request)
