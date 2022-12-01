import datetime
from typing import Union, Optional

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from microservice.dependencies import get_db
from microservice.utils.auth import authenticate_user, get_user_from_token, \
    create_access_token
from microservice.schema.{{ cookiecutter.item_name }}schema import Token


# create the router
user_router = APIRouter(
    prefix="",
    tags=["user"],
)


@user_router.post("/token/", response_model=Token)
async def get_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    # get authenticated user
    user = authenticate_user(
        db=db, 
        username=form_data.username, 
        password=form_data.password
    )
    if user is None:
        # user not found in database
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user/password combination.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # create the JWT token
    access_token = create_access_token({"sub": user.username})

    return {"access_token": access_token, "token_type": "bearer"}
