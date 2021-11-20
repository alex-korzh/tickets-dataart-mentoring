from pydantic import BaseModel
from models.main import StationTypeEnum
from typing import Optional


class StationUpdateDto(BaseModel):
    name: str
    station_type: Optional[StationTypeEnum]


class StationDto(StationUpdateDto):
    id: int
    id_locality: int


class TicketDto(BaseModel):
    id: int
    id_station_departure: int
    id_station_arrival: int
    #passenger_id: int


class UserDto(BaseModel):
    id: int
    id_station_departure: int
    id_station_arrival: int


class LocalityDto(BaseModel):
    id: int
    name: str


class LoginDto(BaseModel):
    email: str
    password: str


class RefreshDto(BaseModel):
    access_token: str


class CredentialsDto(RefreshDto):
    id: int
    refresh_token: str
