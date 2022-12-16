{{ cookiecutter.service_name }}
=======================

setup
-----

during development

::

    python -m venv env
    source env/bin/activate
    pip install -e .


in production

::

    python -m venv env
    source env/bin/activate
    pip install -U {{ cookiecutter.service_name }}


usage
-----

start the micro service

::

    {{ cookiecutter.service_name }} runserver


Point your browser to [http://127.0.0.1:{{ cookiecutter.port }}](http://127.0.0.1:{{ cookiecutter.port }}) to 
access the API.

For the documentation browse to 
[http://127.0.0.1:{{ cookiecutter.port }}/redoc](http://127.0.0.1:{{ cookiecutter.port }}/redoc).


testing client with curl
------------------------

get JWT token
~~~~~~~~~~~~~

::
    
    curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "username=user&password=password" http://127.0.0.1:8000/token/


store the `access_token` for the further calls.


add a {{ cookiecutter.item_name }}
~~~~~~~~~~~~~~

::
    
    curl -d '{"id":"1", "name":"name"}' -H "Content-Type: application/json" -H "Authorization: Bearer <token>" -X POST http://127.0.0.1:8000/{{ cookiecutter.item_name }}s/



get {{ cookiecutter.item_name }} by ID
~~~~~~~~~~~~~~

::
    
    curl -H "Content-Type: application/json" -H "Authorization: Bearer <token>" -X GET http://127.0.0.1:8000/{{ cookiecutter.item_name }}s/<id>/


delete {{ cookiecutter.item_name }} by ID
~~~~~~~~~~~~~~

::
    
    curl -H "Content-Type: application/json" -H "Authorization: Bearer <token>" -X DELETE http://127.0.0.1:8000/{{ cookiecutter.item_name }}s/<id>/




get all {{ cookiecutter.item_name }}s
~~~~~~~~~~~~~~~

::
    
    curl -H "Content-Type: application/json" -H "Authorization: Bearer <token>" -X GET http://127.0.0.1:8000/{{ cookiecutter.item_name }}s/
