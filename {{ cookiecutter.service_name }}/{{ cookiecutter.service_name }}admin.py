import click

from dependencies import pwd_context
from database.db import SessionLocal
from database.models import User


@click.group()
def cli():
    pass


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


if __name__ == "__main__":
    cli()
