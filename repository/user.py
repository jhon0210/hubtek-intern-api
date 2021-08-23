import uuid
from fastapi import HTTPException, Response, status
from sqlalchemy.orm import Session

from .. import models, schemas
from ..hashing import Hash


def list_users(limit: int, db: Session):
    users = db.query(models.User).limit(limit).all()

    return users


def create(req: schemas.User, db: Session):
    new_user = models.User(
        name = req.name,
        last_name = last_name,
        email = req.email,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def find(id, res: schemas.User, db: Session):
    user = db.query(models.User).filter(models.User.public_key == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'The user with the id {id} was not found!'
        )

    return user


def update(id, req: schemas.User, db: Session):
    db.query(models.User) \
        .filter(models.User.public_key == id) \
        .update({
            'name': req.name,
            'last_name': req.last_name,
            'email': req.email,
        })
    db.commit()

    return {'message': f'The user with the id {id} was saved succesfully'}


def destroy(id, db: Session):
    db.query(models.User) \
        .filter(models.User.id == id) \
        .delete(synchcronize_session = False)

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
