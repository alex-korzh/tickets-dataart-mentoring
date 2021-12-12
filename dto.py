from pydantic import BaseModel, validator
from models.main import StationTypeEnum
from typing import Optional, List


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


class FlightDto(BaseModel):
    id: int
    name: str


class FlightListResponse(BaseModel):
    flights: List[FlightDto]


class LocalityListResponse(BaseModel):
    localities: List[LocalityDto]


class StationListResponse(BaseModel):
    stations: List[StationDto]


class TicketListResponse(BaseModel):
    tickets: List[TicketDto]


class UsersListResponse(BaseModel):
    users: List[UserDto]


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


class BuyTicketDto(BaseModel):
    departure_station_id: int
    arrival_station_id: int
    flight_id: int


class TicketBuyResponse(BaseModel):
    name: str
