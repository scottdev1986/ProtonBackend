.PHONY: run format

run:
	uv run fastapi dev --reload

format:
	uv run black --verbose .