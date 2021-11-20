from pydantic import BaseModel, validator
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
    full_name: Optional[str]
    email: str
    is_admin: Optional[bool]
    is_deleted: Optional[bool]
    is_blocked: Optional[bool]


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


class SignupDto(BaseModel):
    email: str
    password: str
    repeated_password: str

    @validator('repeated_password')
    def validate_passwords_match(cls, v, values, **kwargs):
        if v != values['password']:
            raise ValueError('passwords do not match')


