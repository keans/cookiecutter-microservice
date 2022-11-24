from typing import Union

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies import get_db, oauth2_scheme
from schema.{{ cookiecutter.item_name }}schema import {{ cookiecutter.__item_cls }}CreateSchema
from crud.{{ cookiecutter.item_name }}crud import {{ cookiecutter.item_name }}
from database.models import User
from utils.auth import get_current_user

# create the router
{{ cookiecutter.item_name }}_router = APIRouter(
    prefix="",
    tags=["{{ cookiecutter.item_name }}s"],
)


@{{ cookiecutter.item_name }}_router.get("/{{ cookiecutter.item_name }}s/")
async def get_{{ cookiecutter.item_name }}s(
    skip: int = 0, limit: int = 100, 
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    get all {{ cookiecutter.item_name }}s
    """
    return {{ cookiecutter.item_name }}.get_list(db=db, skip=skip, limit=limit)


@{{ cookiecutter.item_name }}_router.get("/{{ cookiecutter.item_name }}s/{id}/")
async def get_{{ cookiecutter.item_name }}(
    id: int, q: Union[str, None] = None, 
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    get {{ cookiecutter.item_name }} by its ID
    """
    item = {{ cookiecutter.item_name }}.get(db=db, id=id)
    if item is None:
        # item not found
        raise HTTPException(
            status_code=404, 
            detail=f"{{ cookiecutter.__item_cls }} with ID {id} not found"
        )

    return item


@{{ cookiecutter.item_name }}_router.post("/{{ cookiecutter.item_name }}s/")
async def create_{{ cookiecutter.item_name }}(
    {{ cookiecutter.item_name }}_schema: {{ cookiecutter.__item_cls }}CreateSchema, 
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    create new {{ cookiecutter.item_name }}
    """
    return {{ cookiecutter.item_name }}.create(db, obj_in={{ cookiecutter.item_name }}_schema)
