.PHONY: deps run test lint format clean

VENV = .venv
PYTHON = $(VENV)/bin/python

deps:
	$(VENV)/bin/pip install -r requirements.txt

run:
	$(PYTHON) -m phoenix

test:
	$(PYTHON) -m pytest

lint:
	$(PYTHON) -m ruff check phoenix tests

format:
	$(PYTHON) -m ruff format phoenix tests

clean:
	rm -rf build dist *.egg-info .pytest_cache .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
