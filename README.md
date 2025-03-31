# django blog

This app requires [uv](https://docs.astral.sh/uv/) to run.

## Instructions to run
Run the following commands to setup the environment:
```bash
uv sync # installs packages
uv run manage.py migrate # creates migrations
```
To run the app, run:
```bash
uv run manage.py runserver # runs the app
```