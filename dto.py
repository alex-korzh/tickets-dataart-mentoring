from dataclasses import dataclass

from pydantic import BaseModel

from models import StationTypeEnum


class StationUpdateDto(BaseModel):
    name: str
    station_type: StationTypeEnum


class StationDto(StationUpdateDto):
    id: int
    id_locality: int


class LoginDto(BaseModel):
    email: str
    password: str


class RefreshDto(BaseModel):
    access_token: str


class CredentialsDto(RefreshDto):
    id: int
    refresh_token: str
