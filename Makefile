.PHONY: activate
activate: _init_venv ## activate the virtualenv associate with this project
	pipenv shell

# @see http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.DEFAULT_GOAL := help
.PHONY: help
help: ## provides cli help for this makefile (default)
	@grep -E '^[a-zA-Z_0-9-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: ci
ci : lint tests ## run continuous integration process

.PHONY: dist
dist: _init_venv
	pipenv run python setup.py sdist

.PHONY: freeze_requirements
freeze_requirements: _init_venv ## update the project dependencies based on setup.py declaration
	pipenv update

.PHONY: install_requirements_dev
install_requirements_dev: _init_venv ## install pip requirements for development
	pipenv install --dev

.PHONY: install_requirements
install_requirements: _init_venv ## install pip requirements based on requirements.txt
	pipenv install

.PHONY: lint
lint: _init_venv ## run pylint
	pipenv run pylint --rcfile=.pylintrc *.py

.PHONY: tests
tests: _init_venv tests_units ## run automatic tests

.PHONY: tests_units
tests_units: ## run only unit tests
	pipenv run python -u -m unittest discover

# If a directory .venv is present in the project folder,
# pipenv will use this directory to instanciate a virtualenv
# instead of doing it in your localdata.
#
# Doing it make easier the sharing of debug configuration between
# IDE like vscode or pycharm.
#
# The issue is pipenv --rm will remove all the .venv directory and .gitkeep file.
# this instruction ensure the directory is present even if the virtual environment
# has been remove.
.PHONY: _init_venv
_init_venv:
	mkdir -p .venv && touch .venv/.gitkeep
