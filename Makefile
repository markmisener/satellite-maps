SHELL := /bin/bash

.PHONY: install clean pre-commit

venv:
	virtualenv --python=python3.6 dev-env

install: venv
	source dev-env/bin/activate; \
	pip install -r requirements.txt; \

clean:
	rm -r dev-env/

pre-commit: install
	source dev-env/bin/activate; \
	pre-commit run --all-files

run-local: install
	source dev-env/bin/activate; \
	sh start.sh
