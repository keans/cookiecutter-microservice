from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from microservice.database.db import SessionLocal


# authentication scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# password context
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def get_db():
    """
    get the database for the Dependency
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

