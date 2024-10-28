# Dockerfile
FROM python:3.12.7-slim

WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy the poetry files to install dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the app source
COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]