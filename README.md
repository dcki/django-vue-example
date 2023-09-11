- Install Python 3.11 (for example, with pyenv)
- Install Poetry
- `python3 -m venv .venv`
- `poetry env use .venv`
- `poetry install`
- `source .venv/bin/activate`
- `python3 manage.py migrate`
- `python3 manage.py shell <<EOF`
- `from notes.models import Note`
- `Note.objects.create(content='Trees are great.')`
- `EOF`
- `python3 manage.py runserver`
- View [http://127.0.0.1:8000/notes/](http://127.0.0.1:8000/notes/)

To do:
- When client receives 403 response, determine if it's due to an invalid CSRF token (which indicates a client-side bug) or due to the user not having permission. Or, should CSRF failure respond with 401 instead?
- Production:
    - Update Django settings.
    - Use production version of Vue.
