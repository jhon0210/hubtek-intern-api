from fastapi import APIRouter, Depends, HTTPException, status
from .. import database, models, schemas, token
from sqlalchemy.orm import Session

router = APIRouter(tags=['Auth'])

@router.post('/login')
def login(req: schemas.Login, db: Session=Depends(database.get_db)):
    user = db.query(models.User) \
        .filter(models.User.email == req.username) \
        .first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = 'Invalid credentials'
        )


    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(data={'sub': user.email})

    return {'access_token': access_token, 'token_type': 'bearer'}
