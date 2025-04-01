FROM python:3.13.2-alpine3.21
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /djangoblog


COPY . .
RUN uv sync --frozen
RUN uv run manage.py migrate

EXPOSE 8000
CMD ["uv", "run", "manage.py", "runserver", "0.0.0.0:8000"]