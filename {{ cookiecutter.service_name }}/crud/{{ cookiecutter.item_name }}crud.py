from crud.base import CRUDBase
from database.models import {{ cookiecutter.__item_cls }}


class CRUD{{ cookiecutter.__item_cls }}(CRUDBase[{{ cookiecutter.__item_cls }}]):
    """
    CRUD class for {{ cookiecutter.__item_cls }}
    """


# create an instance of the CRUD{{ cookiecutter.__item_cls }} class
{{ cookiecutter.item_name }} = CRUD{{ cookiecutter.__item_cls }}({{ cookiecutter.__item_cls }})
