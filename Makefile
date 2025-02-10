.PHONY: run format

run:
	uv run fastapi dev --reload

format:
	black --exclude .venv --exclude uv.lock --exclude pyproject.toml --exclude Makefile .