# {{ cookiecutter.service_name }}


## setup

```
python -m venv env
source env/bin/activate
pip install fastapi "uvicorn[standard] sqlalchemy"
```

## usage

start the micro service

```
uvicorn {{ cookiecutter.service_name }}:app --reload
```

Point your browser to [http://127.0.0.1:8000](http://127.0.0.1:8000) to 
access the API.

For the documentation browse to 
[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).


### get JWT token

```
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "username=user&password=password" http://127.0.0.1:8000/token/
```

store the `access_token` for the further calls.


### add a {{ cookiecutter.item_name }}

```
curl -d '{"id":"1", "name":"name"}' -H "Content-Type: application/json" -H "Authorization: Bearer <token>" -X POST http://127.0.0.1:8000/{{ cookiecutter.item_name }}s/
```


### get all {{ cookiecutter.item_name }}s

```
curl -H "Content-Type: application/json" -H "Authorization: Bearer <token>" -X GET http://127.0.0.1:8000/{{ cookiecutter.item_name }}s/
```
