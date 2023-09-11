FROM python:3.11.5-slim-bookworm

WORKDIR /app/

RUN apt update && apt install -y \
    curl \
&& rm -rf /var/lib/apt/lists/*

# Install Poetry
# Explicitly using /bin/bash is necessary because Docker uses /bin/sh,
# which is dart on Debian, which doesn't support `set -o pipefail`.
RUN ["/bin/bash", "-c", "set -o pipefail && curl -sSL https://install.python-poetry.org | python3 -"]

RUN /root/.local/bin/poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock /app/

RUN /root/.local/bin/poetry install

COPY . /app/

CMD python3 manage.py runserver 0.0.0.0:8000
