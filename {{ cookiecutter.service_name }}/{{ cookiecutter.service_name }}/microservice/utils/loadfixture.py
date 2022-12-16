from pathlib import Path
from typing import Union

import yaml
import sqla_yaml_fixtures

from ..database.db import SessionLocal, BaseModel


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

    def dumpdata(self):
        """
        dump data loaded from yaml file to the database
        """
        if not self.filename.exists():
            # file does not exist
            raise LoadFixtureException(
                f"The file '{self.filename}' does not exist! Abort."
            )

        # read text of yaml file
        with self.filename.open("r") as f:
            yml = f.read()

        # prepare DB session
        db = SessionLocal()

        # add data to database
        sqla_yaml_fixtures.load(BaseModel, db, yml)
