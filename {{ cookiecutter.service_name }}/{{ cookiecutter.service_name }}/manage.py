#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import uvicorn

from .microservice.dependencies import pwd_context
from .microservice.database.db import SessionLocal
from .microservice.database.models import User
from .microservice.utils.loadfixture import LoadFixture
from .microservice.{{ cookiecutter.service_name }} import app
from .microservice.utils.config import PORT


@click.group()
def cli():
    pass


@cli.command()
def runserver():
    """
    serve the microservice
    """
    uvicorn.run(
        (
            "{{ cookiecutter.service_name }}.microservice."
            "{{ cookiecutter.service_name }}:app"
        ), 
        port=PORT, 
        log_level="info",
        reload=True
    )


@cli.command()
@click.argument("username")
@click.argument("password")
def createuser(username: str, password: str):
    """
    create a new user
    """
    click.echo(f"Creating user '{username}'...")
    db = SessionLocal()

    # create the user
    user = User(
        username=username, 
        password_hash=pwd_context.hash(password),
        disabled=False
    )
    db.add(user)
    db.commit()


@cli.command()
@click.argument("yamlfile")
def loaddata(yamlfile):
    """
    load data from fixture
    """
    click.echo(f"loading '{yamlfile}'...")
    lf = LoadFixture(filename=yamlfile)
    lf.dumpdata()



if __name__ == "__main__":
    cli()
