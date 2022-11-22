from typing import List, Union

from schema.base import BaseSchema


class {{ cookiecutter.__item_cls }}BaseSchema(BaseSchema):
    """
    """
    name: str


class {{ cookiecutter.__item_cls }}CreateSchema({{ cookiecutter.__item_cls }}BaseSchema):
    """
    """


class {{ cookiecutter.__item_cls }}UpdateSchema({{ cookiecutter.__item_cls }}BaseSchema):
    """
    """
