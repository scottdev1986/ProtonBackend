.PHONY: run format

run:
	uv run fastapi dev --reload

format:
	black --verbose .