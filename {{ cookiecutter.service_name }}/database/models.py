from typing import Union
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.db import BaseModel


class User(BaseModel):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    disabled = Column(Boolean)


class {{ cookiecutter.__item_cls }}(BaseModel):
    __tablename__ = "{{ cookiecutter.item_name.lower() }}s"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
