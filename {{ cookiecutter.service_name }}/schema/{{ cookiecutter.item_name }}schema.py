from typing import List, Union

from pydantic import BaseModel

from schema.base import BaseSchema


class Token(BaseModel):
    access_token: str
    token_type: str


class {{ cookiecutter.__item_cls }}BaseSchema(BaseSchema):
    """
    base schema for {{ cookiecutter.__item_cls }}
    """
    name: str


class {{ cookiecutter.__item_cls }}CreateSchema({{ cookiecutter.__item_cls }}BaseSchema):
    """
    create schema for {{ cookiecutter.__item_cls }}
    """


class {{ cookiecutter.__item_cls }}UpdateSchema({{ cookiecutter.__item_cls }}BaseSchema):
    """
    update schema for {{ cookiecutter.__item_cls }}
    """
