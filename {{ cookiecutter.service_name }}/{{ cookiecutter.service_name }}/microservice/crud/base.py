from typing import TypeVar, Optional, Generic, Any, List

from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from ..database.models import BaseModel


ModelType = TypeVar("ModelType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType]):
    """
    base class from which all CRUD operations shall be derived
    """
    def __init__(
        self, 
        model: ModelType
    ):
        self.model = model
    
    def get(
        self, 
        db: Session,
        id: Any
    ) -> Optional[ModelType]:
        """
        returns the model item that matches the id

        :param db: datanase session
        :type db: Session
        :param id: id of the item
        :type id: Any
        :return: model item
        :rtype: Optional[ModelType]
        """
        return db.query(self.model).filter(
            self.model.id == id
        ).first()
    
    def get_list(
        self,
        db: Session, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[ModelType]:
        """
        returns a list of the model

        :param db: database session
        :type db: Session
        :param skip: skip items, defaults to 0
        :type skip: int, optional
        :param limit: limit the number of results, defaults to 100
        :type limit: int, optional
        :return: list of model items
        :rtype: List[ModelType]
        """
        return db.query(
            self.model
        ).offset(skip).limit(limit).all()


    def create(
        self, 
        db: Session, 
        obj_in: CreateSchemaType
    ) -> ModelType:
        """
        create model item

        :param db: database session
        :type db: Session
        :param obj_in: input schema
        :type obj_in: CreateSchemaType
        :return: created model item
        :rtype: ModelType
        """
        # encode input data
        obj_in_data = jsonable_encoder(obj_in)

        # create database object
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        return db_obj

    def delete(
        self,
        db: Session, 
        id: Any
    ) -> bool:
        """
        delete model item

        :param db: database session
        :type db: Session
        :param id: id of the item
        :type id: Any
        :return: True, if item was found and deleted else False
        :rtype: bool

        """
        item = db.query(self.model).filter(
            self.model.id == id
        ).first()
        if item is None:
            # item not found
            return False
    
        db.delete(item)
        db.commit()
    
        return True

    def update(
        self, 
        db: Session, 
        id: Any,
        obj_in: UpdateSchemaType
    ) -> ModelType:
        """
        update model item

        :param db: database session
        :type db: Session
        :param id: id of the item
        :type id: Any
        :param obj_in: input schema
        :type obj_in: UpdateSchemaType
        :return: updated model item
        :rtype: ModelType
        """
        item = db.query(self.model).filter(
            self.model.id == id
        ).first()
        if item is None:
            # item not found
            return None

        # get dictionary of input data and set these at properties
        obj_in_data = obj_in.dict(exclude_unset=True)
        for key, value in obj_in_data.items():
            setattr(item, key, value)

        db.add(item)
        db.commit()
        db.refresh(item)
        
        return item
