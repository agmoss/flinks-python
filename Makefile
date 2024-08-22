.PHONY: init qa lint tests spec coverage


init:
	pipenv install --three --dev


# DEVELOPMENT
# ~~~~~~~~~~~
# The following rules can be used during development in order to get a Python shell, etc.
# --------------------------------------------------------------------------------------------------

shell:
	pipenv shell


# QUALITY ASSURANCE
# ~~~~~~~~~~~~~~~~~
# The following rules can be used to check code quality, import sorting, etc.
# --------------------------------------------------------------------------------------------------

qa: format isort lint

# Code quality checks (eg. flake8, eslint, etc).
lint:
	pipenv run flake8

format:
	black pyflinks

# Import sort checks.
isort:
	isort pyflinks


# TESTING
# ~~~~~~~
# The following rules can be used to trigger tests execution and produce coverage reports.
# --------------------------------------------------------------------------------------------------

# Just runs all the tests!
tests:
	pipenv run py.test

# Collects code coverage data.
coverage:
	pipenv run py.test --cov-report term-missing --cov flinks

# Run the tests in "spec" mode.
spec:
	pipenv run py.test --spec -p no:sugar

typecheck:
	mypy ./$(pyflinks) --check-untyped-defs

clean: clean-build clean-pyc clean-test clean-mypy

clean-build:
	$(RM) -fr build/
	$(RM) -fr dist/
	$(RM) -fr .eggs/
	find . -name '*.egg-info' -exec $(RM) -fr {} +
	find . -name '*.egg' -exec $(RM) -f {} +

clean-pyc:
	find . -name '*.pyc' -exec $(RM) -f {} +
	find . -name '*.pyo' -exec $(RM) -f {} +
	find . -name '*~' -exec $(RM) -f {} +
	find . -name '__pycache__' -exec $(RM) -fr {} +

clean-mypy:
	$(RM) -fr .mypy_cache/

clean-test:
	$(RM) -fr .pytest_cache

release: dist
	twine upload dist/*

dist: clean
	python setup.py sdist bdist_wheel
	ls -l dist
