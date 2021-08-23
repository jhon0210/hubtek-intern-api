from fastapi import FastAPI

from . import models
from .database import engine
from .routers import dog, user

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(dog.router)

