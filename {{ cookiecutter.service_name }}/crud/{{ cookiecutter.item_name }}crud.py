from crud.base import CRUDBase
from database.models import {{ cookiecutter.__item_cls }}


class CRUD{{ cookiecutter.__item_cls }}(CRUDBase[{{ cookiecutter.__item_cls }}]):
    """
    """


{{ cookiecutter.item_name }} = CRUD{{ cookiecutter.__item_cls }}({{ cookiecutter.__item_cls }})
