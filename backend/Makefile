SHELL := /bin/bash

VENV=.venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

.PHONY: setup update activate clean

setup:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	if [ -f requirements.txt ]; then \
		$(PIP) install -r requirements.txt; \
		echo "requirements.txt found. Installation successful."; \
	else \
		echo "requirements.txt not found. Skipping installation."; \
	fi

update:
	$(PIP) freeze > requirements.txt

clean:
	rm -rf $(VENV)