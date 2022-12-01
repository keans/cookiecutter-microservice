#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import requests
import uvicorn

from microservice.dependencies import pwd_context
from microservice.database.db import SessionLocal
from microservice.database.models import User
from microservice.utils.config import CMD_USER, CMD_PASSWORD
from microservice.{{ cookiecutter.service_name }} import app


@click.group()
def cli():
    pass


@cli.command()
def runserver():
    """
    serve the microservice
    """
    uvicorn.run(
        "microservice.{{ cookiecutter.service_name }}:app", 
        port=8000, 
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

    user = User(
        username=username, 
        password_hash=pwd_context.hash(password),
        disabled=False
    )
    db.add(user)
    db.commit()



@cli.command()
@click.option(
    "-u", "--username", 
    default=CMD_USER,
    required=True
)
@click.option(
    "-p", "--password", 
    default=CMD_PASSWORD,
    required=True
)
def gettoken(username: str, password: str):
    """
    get OAuth2 bearer token
    """
    headers = {
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data = {
        "username": username,
        "password": password
    }   
    r = requests.post(
        f"http://127.0.0.1:8000{app.url_path_for('get_access_token')}", 
        data=data, 
        headers=headers
    )
    if "access_token" not in r.json():
        # access token could not be obtained
        raise click.ClickException(
            f"could not obtain the access token: {r.json()}"
        )

    click.echo(r.json()["access_token"])


if __name__ == "__main__":
    cli()
