from pathlib import Path
from typing import Union
import importlib

import yaml

from microservice.database.db import SessionLocal


class LoadFixtureException(Exception):
    """
    load fixture exception
    """


class LoadFixture:
    """
    helper class to load fixtures from a yaml file
    and store them in the target database
    """
    def __init__(self, filename: Union[Path, str], auto_load=True):
        self.filename = (
            filename
            if isinstance(filename, Path) else
            Path(filename)
        )

        self.li = []
        if auto_load is True:
            # load the fixture
            self.li = self.load()

    def load(self) -> list:
        """
        load the fixtures from yaml file
        """
        if not self.filename.exists():
            # file does not exist
            raise LoadFixtureException(
                f"The file '{self.filename}' does not exist! Abort."
            )
        
        with self.filename.open("r") as f:
            return yaml.safe_load(f)

    def dumpdata(self):
        """
        dump data loaded from yaml file to the database
        """
        # get module of models
        module = importlib.import_module("microservice.database.models")

        # prepare DB session
        db = SessionLocal()
        for item in self.li:
            # get class based on model name
            cls = getattr(module, item["model"])

            # create model instance with provided fields
            m = cls(id=item["pk"], **item["fields"])

            # add model instance to the database
            db.add(m)
            db.commit()
