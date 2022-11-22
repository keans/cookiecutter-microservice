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


add an item

```
curl -d '{"id":"1", "name":"cool"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/items/
```
