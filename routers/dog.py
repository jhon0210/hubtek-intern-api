from typing import List, Optional
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session

from .. import models, oauth2, schemas
from ..database import get_db
from ..repository import dog

router = APIRouter(
    prefix = '/dogs',
    tags = ['Dogs']
)


@router.get('/', response_model=List[schemas.ShowDog])
def list_dogs(
        limit: int=10,
        db: Session=Depends(get_db),
        get_current_user: schemas.User=Depends(oauth2.get_current_user)):
    return dog.list_dogs(limit, db)


@router.get('/{name}', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowDog])
def find_dogs(
        name,
        db: Session=Depends(get_db),
        get_current_user: schemas.User=Depends(oauth2.get_current_user)):
    return dog.find_matches(name, response)


@router.get('/is_adopted', status_code=status.HTTP_200_OK, response_model=schemas.ShowDog)
def find_adopted_dog(db: Session=Depends(get_db)):
    pass


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowDog)
def create_dog(
        req: schemas.Dog,
        db: Session=Depends(get_db),
        get_current_user: schemas.User=Depends(oauth2.get_current_user)):
    return dog.create(req, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_dog(
        id,
        req: schemas.Dog,
        db: Session=Depends(get_db),
        get_current_user: schemas.User=Depends(oauth2.get_current_user)):
    return dog.update(id, req, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_dog(
        id,
        db: Session=Depends(get_db),
        get_current_user: schemas.User=Depends(oauth2.get_current_user)):
    return dog.destroy(id, db)

