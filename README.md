# django blog

This app requires docker to run.

## Instructions to run
Run the following commands to setup the environment and run the program:
```bash
docker compose up --build
```

## Using ruff

Use ruff to lint over code:
```bash
uv run ruff check
```
Do the above command inside the docker container. It causes error when ran locally (idk why)