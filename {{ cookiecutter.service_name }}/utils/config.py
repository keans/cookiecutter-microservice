import os
from uuid import uuid4

from dotenv import load_dotenv

# load .env file
load_dotenv()


# database URL
SQLALCHEMY_DATABASE_URL = os.environ.get(
    "{{ cookiecutter.service_name.upper() }}_DB",
    default="sqlite:///{{ cookiecutter.service_name.lower() }}.db"
)


# token expiration in minutes for JWT
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get(
    "{{ cookiecutter.service_name.upper() }}_ACCESS_TOKEN_EXPIRE_MINUTES",
    default=30
)

# secret key for JWT
JWT_SECRET_KEY =  os.environ.get(
    "{{ cookiecutter.service_name.upper() }}_JWT_SECRET_KEY",
    default="{{ uuid4() }}"
)

# algorithm for JWT
JWT_ALGORITHM = os.environ.get(
    "{{ cookiecutter.service_name.upper() }}_JWT_ALGORITHM",
    default="HS256"
)
