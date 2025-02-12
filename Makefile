.PHONY: run format test

run:
	uv run fastapi dev --reload

format:
	uv run black --verbose .

FILE ?= .
test:
	uv run pytest tests/$(FILE)