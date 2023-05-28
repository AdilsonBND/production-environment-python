.PHONY: clean
clean:
	rd /s .\.venv\ .\.pytest_cache\ .\src\__pycache__\

.PHONY: install
install:
	poetry install --with test,lint
	poetry run pre-commit install --hook-type pre-commit --hook-type commit-msg --hook-type pre-push

.PHONY: test
test:
	poetry run python -m pytest
