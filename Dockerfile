FROM python:3.13.2-alpine3.21

WORKDIR /djangoblog

COPY . .
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV TZ America/New_York
ENV C_FORCE_ROOT true

RUN apk update && \
    apk add bash git && \
    uv sync --frozen && \
    uv run manage.py makemigrations blog oauth && \
    uv run manage.py migrate


CMD ["uv", "run", "manage.py", "runserver", "0.0.0.0:8000"]