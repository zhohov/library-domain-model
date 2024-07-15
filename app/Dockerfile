FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN pip install --upgrade pip && pip install poetry
RUN poetry install --no-dev --no-interaction --no-ansi

COPY . /app/

EXPOSE 8000

CMD ["poetry", "run", "pytest"]

