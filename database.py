from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

POSTGRES_DBHOST = os.getenv('POSTGRES_DBHOST')
POSTGRES_DBNAME = os.getenv('POSTGRES_DBNAME')
POSTGRES_DBPORT = os.getenv('POSTGRES_DBPORT')
DB_USER         = os.getenv('DB_USER')
DB_PASSWORD     = os.getenv('DB_PASSWORD')

DATABASE_URL    = f'postgresql://{DB_USER}:{DB_PASSWORD}@{POSTGRES_DBHOST}:{POSTGRES_DBPORT}/{POSTGRES_DBNAME}'

engine = create_engine(
    DATABASE_URL,
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

