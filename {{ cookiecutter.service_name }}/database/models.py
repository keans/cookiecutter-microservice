from typing import Union
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.db import BaseModel, engine


class User(BaseModel):
    """
    User model
    """
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password_hash = Column(String)
    disabled = Column(Boolean)


class {{ cookiecutter.__item_cls }}(BaseModel):
    """
    {{ cookiecutter.__item_cls }} model
    """
    __tablename__ = "{{ cookiecutter.item_name.lower() }}s"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)


# create all tables
BaseModel.metadata.create_all(bind=engine)
