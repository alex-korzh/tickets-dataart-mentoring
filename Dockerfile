FROM python:3.9


ENV FLASK_APP=main \
    FLASK_ENV=development \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_RUN_PORT=8000 \
    FLASK_RUN_HOST=0.0.0.0


RUN pip3 install poetry

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN poetry config virtualenvs.create false && poetry install --no-interaction

COPY . /app

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD ["/entrypoint.sh"]
EXPOSE 8000
