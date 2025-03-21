.PHONY: sync
sync:
	poetry sync --with test,example

.PHONY: tests
tests:
	poetry run pytest

.PHONY: format
format:
	poetry run ruff format

.PHONY: lint
lint:
	poetry run ruff check

.PHONY: examples
examples:
	poetry run python examples/tool.py
	poetry run python examples/ai_tool.py
