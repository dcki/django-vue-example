This is an example Django and Vue app.

How to set up the local development environment:

- Install Docker
- Install Python 3.11 (for example, with pyenv)
- Install Poetry
- Then run the following commands:
- `docker network create django-vue-example`
- `docker run -e POSTGRES_HOST_AUTH_METHOD=trust --net django-vue-example -p 5432:5432 --name=postgres -itd postgres:15`
- `docker exec -it postgres createdb -U postgres django-vue-example`

How to run the app locally:

- `brew install libpq` or `apt install libpq-dev`
- On mac: `echo 'export PATH="/usr/local/opt/libpq/bin:$PATH"' >> ~/.profile` On others: Something similar.
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
- View [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Stop the server with `^C` (`ctrl-c`)

How to run the app locally in Docker:

- `docker container stop django-vue-example; docker container rm django-vue-example; docker build --tag django-vue-example --progress=plain . && docker run -e DB_HOST=postgres --net django-vue-example -p 8000:8000 --name django-vue-example -it django-vue-example`
- In another shell:
- `docker exec -it django-vue-example python3 manage.py migrate`
- `docker exec -it django-vue-example bash`
- `python3 manage.py shell <<EOF`
- `from notes.models import Note`
- `Note.objects.create(content='Trees are great.')`
- `EOF`
- `exit`
- View [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

To do:

- Use Docker Compose.
- Use a volume with the postgres container.
- Apply the recommendations from the Django database documentation [general notes](https://docs.djangoproject.com/en/4.2/ref/databases/#general-notes) and [PostgreSQL notes](https://docs.djangoproject.com/en/4.2/ref/databases/#postgresql-notes)
- When client receives 403 response, determine if it's due to an invalid CSRF token (which indicates a client-side bug) or due to the user not having permission. Or, should CSRF failure respond with 401 instead?
- Production:
    - Use Gunicorn and Nginx.
    - Update Django settings.
    - Use production version of Vue.
    - Run database migrations inside VPC (datacenter) instead of from laptop.
