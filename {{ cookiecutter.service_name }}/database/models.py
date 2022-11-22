from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.db import BaseModel


class {{ cookiecutter.__item_cls }}(BaseModel):
    __tablename__ = "{{ cookiecutter.item_name.lower() }}s"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
