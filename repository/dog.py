from fastapi import HTTPException, Response, status
from sqlalchemy.orm import Session

from .. import models, schemas

def list_dogs(limit: int, is_adopted: bool, db: Session):
    if is_adopted == None:
        dogs = db.query(models.Dog).limit(limit).all()
    else:
        dogs = db.query(models.Dog) \
                .where(models.Dog.is_adopted == is_adopted) \
                .limit(limit).all()

    return dogs


def create(req: schemas.Dog, db: Session):
    new_dog = models.Dog(
        name = req.name,
        picture = req.picture,
        is_adopted = req.is_adopted,
    )

    db.add(new_dog)
    db.commit()
    db.refresh(new_dog)
    return new_dog

