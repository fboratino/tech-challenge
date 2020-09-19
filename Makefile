.PHONY: lint

help:
	@echo "lint - check style with flake8"

lint:
	SKIP=no-commit-to-branch pre-commit run -a -v