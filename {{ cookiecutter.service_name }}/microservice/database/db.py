from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from microservice.utils.config import SQLALCHEMY_DATABASE_URL


# create database engine for given database URL
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

# perpare local session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create base model from which all database models shall be derived
BaseModel = declarative_base()
