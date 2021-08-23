from fastapi import HTTPException, Response, status
from sqlalchemy.orm import Session
import requests

from .. import models, schemas

DOGS_PICTURES_API = 'https://dog.ceo/api/breeds/image/random'

def list_dogs(limit: int, db: Session):
    dogs = db.query(models.Dog).limit(limit).all()

    return dogs


def create(req: schemas.Dog, db: Session):
    response = requests.get(DOGS_PICTURES_API)
    picture = response.json()['message']

    new_dog = models.Dog(
        name = req.name,
        picture = picture,
        is_adopted = req.is_adopted,
    )

    db.add(new_dog)
    db.commit()
    db.refresh(new_dog)
    return new_dog

