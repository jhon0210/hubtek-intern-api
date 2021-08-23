from fastapi import HTTPException, Response, status
from sqlalchemy.orm import Session
import requests

from .. import models, schemas

DOGS_PICTURES_API = 'https://dog.ceo/api/breeds/image/random'

def list_dogs(limit: int, db: Session):
    dogs = db.query(models.Dog).limit(limit).all()

    return dogs


def find_matches(name: str, db: Session):
    ilike_name = '%' + name + '%'
    dogs = db.query(models.Dog) \
            .filter(models.Dog.name.ilike(ilike_name))

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


def update(id, req: schemas.Dog, db: Session):
    db.query(models.Dog) \
        .filter(models.Dog.id == id) \
        .update({
            'name': req.name,
            'is_adopted': req.name
        })
    db.commit()

    return {'message': f'The dog with the id {id} was saved succesfully'}


def destroy(id, db: Session):
    db.query(models.Dog) \
        .filter(models.Dog.id == id) \
        .delete(synchcronize_session = False)

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
