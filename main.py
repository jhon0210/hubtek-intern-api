from fastapi import FastAPI

from . import models
from .database import engine
from .routers import dog, user, auth

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(auth.router)
app.include_router(dog.router)
app.include_router(user.router)

