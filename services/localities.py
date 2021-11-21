from typing import List
from dto import LocalityDto
from models import Locality


class LocalityService:
    @staticmethod
    def get_all() -> List[LocalityDto]:
        localities = Locality.query.all()
        return [LocalityDto(**s.to_dict()) for s in localities]

    @staticmethod
    def get_one_by_id(id: int) -> LocalityDto:
        rez_localities = Locality.query.get(id)
        return LocalityDto(**rez_localities.to_dict())

