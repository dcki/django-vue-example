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
- Production:
    - Update Django settings.
    - Use production version of Vue.
