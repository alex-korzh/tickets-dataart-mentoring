from dataclasses import dataclass

from models import StationTypeEnum


@dataclass
class StationUpdateDto:
    name: str
    station_type: StationTypeEnum


@dataclass
class StationDto(StationUpdateDto):
    id: int
    id_locality: int
