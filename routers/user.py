from typing import List, Optional
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session

from .. import models, oauth2, schemas
from ..database import get_db
from ..repository import user

router = APIRouter(
    prefix='/users',
    tags = ['Users']
)


@router.get('/', response_model = List[schemas.User])
def list_users(limit: int=10, active: Optional[bool]=None, db: Session=Depends(get_db)):
    return user.list_users(limit, active, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.User)
def find_user(id, res: Response, db: Session = Depends(get_db)):
    return user.find(id, res, db)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.User)
def create_user(req: schemas.User, db: Session=Depends(get_db)):
    return user.create(req, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_user(id, req: schemas.User, db: Session=Depends(get_db)):
    return user.update(id, req, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_user(id, db: Session=Depends(get_db)):
    return user.destroy(id, db)

