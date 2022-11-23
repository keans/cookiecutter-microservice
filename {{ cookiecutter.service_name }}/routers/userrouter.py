from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from dependencies import get_db, pwd_context
from database.models import User


# create the router
user_router = APIRouter(
    prefix="",
    tags=["user"],
)


@user_router.post("/token/")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
     db: Session = Depends(get_db)
):
    # get user from database
    user = db.query(User).filter(
        User.username == form_data.username
    ).first()
    if user is None:
        # user not found in database
        raise HTTPException(
            status_code=400, 
            detail="Incorrect username or password"
        )

    # check password
    if pwd_context.verify(form_data.password, user.password_hash) is False:
        # invalid password
        raise HTTPException(
            status_code=400, 
            detail="Incorrect username or password"
        )

    return {"access_token": user.username, "token_type": "bearer"}
