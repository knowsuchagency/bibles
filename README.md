A dead-simple REST API for the bible made with django-rest-framework. An example deployment can be found [HERE](https://bibler.herokuapp.com).

If you want to run it locally on localhost:8000 clone the project and run the following commands:

```
pip install -r requirements.txt
python manage.py migrate
python seed.py
python manage.py runserver
```
