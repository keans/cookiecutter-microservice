import os

from dotenv import load_dotenv

load_dotenv()


SQLALCHEMY_DATABASE_URL = os.environ.get(
    "{{ cookiecutter.service_name.upper() }}_DB",
    "sqlite:///{{ cookiecutter.service_name.lower() }}.db"
)
