FROM python:3.13.2-alpine3.21
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV TZ America/New_York
ENV C_FORCE_ROOT true

RUN apk update && \
    apk add bash git

WORKDIR /djangoblog