#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Union
from unittest import skip

from fastapi import FastAPI, HTTPException

from database.db import engine, BaseModel
from routers.userrouter import user_router
from routers.{{ cookiecutter.item_name }}router import {{ cookiecutter.item_name }}_router


# create tables
BaseModel.metadata.create_all(bind=engine)


# prepare API application
app = FastAPI(
    title="{{ cookiecutter.__item_cls }} API",
)

app.include_router({{ cookiecutter.item_name }}_router)
app.include_router(user_router)


@app.get("/")
async def get_version() -> dict:
    """
    returns basic information about the service

    :return: basic service information
    :rtype: dict
    """
    return {
        "service": "{{ cookiecutter.service_name }}",
        "description": "{{ cookiecutter.description }}",
        "author": "{{ cookiecutter.author }}",
        "email": "{{ cookiecutter.email }}",
        "version": "{{ cookiecutter.version }}"
    }


