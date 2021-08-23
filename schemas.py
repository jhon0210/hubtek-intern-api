from pydantic import BaseModel
from typing import Optional
import datetime


class Dog(BaseModel):
    name: str
    is_adopted: bool


class ShowDog(BaseModel):
    id: int
    name: str
    picture: str
    is_adopted: bool
    create_date: datetime.datetime

    class Config:
        orm_mode = True

