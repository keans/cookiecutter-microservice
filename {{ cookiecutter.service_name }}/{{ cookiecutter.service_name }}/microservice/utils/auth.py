import datetime
from typing import Optional, Union

from sqlalchemy.orm import Session
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from ..dependencies import pwd_context, get_db, oauth2_scheme
from ..database.models import User
from ..utils.config import JWT_ACCESS_TOKEN_EXPIRE_MINUTES, \
    JWT_ALGORITHM, JWT_SECRET_KEY


def get_user_by_name(db: Session, username: str) -> Optional[User]:
    """
    get the user from the database by the user's name

    :param db: database session
    :type db: Session
    :param username: username
    :type username: str
    :return: the user or None, if it is not existing
    :rtype: Optional[User]
    """
    return db.query(User).filter(User.username == username).first()


def authenticate_user(db: Session, username: str, password: str) -> bool:
    """
    authenticate user, i.e., return True if given user exists and password
    is correct else return False

    :param db: database session
    :type db: Session
    :param username: usernmae
    :type username: str
    :param password: password
    :type password: str
    :return: user, if user/password combination exists else None
    :rtype: bool
    """
    # get user from database
    user = get_user_by_name(db=db, username=username)
    if user is None:
        # user not found
        return None
    
    # user found, then check password
    if pwd_context.verify(password, user.password_hash) is False:
        # wrong password
        return None
    
    return user


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> Optional[User]:
    """
    get the user by given token

    :param token: token, defaults to Depends(oauth2_scheme)
    :type token: str, optional
    :param db: database session, defaults to Depends(get_db)
    :type db: Session, optional
    :return: return the current user
    :rtype: Optional[User]
    """
    # get the user by given token
    user = get_user_from_token(db=db, token=token)
    if user is None:
        # user could not be obtained from token
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if user.disabled:
        # user is disabled
        raise HTTPException(
            status_code=400,
            detail="Inactive user."
        )

    return user


def get_user_from_token(
    db: Session,
    token: OAuth2PasswordBearer
) -> Optional[User]:
    """
    get user from jwt token

    :param db: database session
    :type db: Session
    :param token: oauth2 password token
    :type token: OAuth2PasswordBearer
    :return: user or None, if token cannot be parsed
    :rtype: Optional[User]
    """
    try:
        # decode the token
        payload = jwt.decode(
            token, 
            key=JWT_SECRET_KEY, 
            algorithms=[JWT_ALGORITHM]
        )

        # get user from token
        username = payload.get("sub")
        if username is None:
            # username not found
            return None

    except JWTError:
        # some JWT error
        return None

    return get_user_by_name(db=db, username=username)


def create_access_token(
    data: dict, 
    expires_delta: Union[datetime.timedelta, None] = None
):
    # compute expiration date (use provided delta or default value from config)
    expiration_date = (
        datetime.datetime.utcnow() + 
        (
            expires_delta or 
            datetime.timedelta(minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
        )
    )
    print(expiration_date)
    
    # encode the JWT data
    encoded_jwt = jwt.encode(
        claims={**data, **{"exp": expiration_date}}, 
        key=JWT_SECRET_KEY, 
        algorithm=JWT_ALGORITHM
    )

    return encoded_jwt
