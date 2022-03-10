VENV_NAME?=venv
PIP?=pip3
PYTHON?=python3

venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: setup.py
	$(PIP) install --upgrade pip virtualenv
	@test -d $(VENV_NAME) || $(PYTHON) -m virtualenv --clear $(VENV_NAME)
	${VENV_NAME}/bin/python -m pip install -U pip tox
	${VENV_NAME}/bin/python -m pip install -e .
	@touch $(VENV_NAME)/bin/activate

run: venv
	@${VENV_NAME}/bin/python examples/sample.py

test: venv
	@${VENV_NAME}/bin/tox -p auto $(TOX_ARGS)

test-nomock: venv
	@${VENV_NAME}/bin/tox -p auto -- --nomock $(TOX_ARGS)

test-travis: venv
	${VENV_NAME}/bin/python -m pip install -U tox-travis
	@${VENV_NAME}/bin/tox -p auto $(TOX_ARGS)

fmt: venv
	@${VENV_NAME}/bin/tox -e fmt

fmtcheck: venv
	@${VENV_NAME}/bin/tox -e fmt -- --check --verbose

lint: venv
	@${VENV_NAME}/bin/tox -e lint

publish-test: test
	${VENV_NAME}/bin/python -m pip install --upgrade twine
	${VENV_NAME}/bin/python -m twine upload --repository testpypi .tox/dist/*

publish: test
	${VENV_NAME}/bin/python -m pip install --upgrade twine
	${VENV_NAME}/bin/python -m twine upload --repository pypi .tox/dist/*

clean:
	@rm -rf $(VENV_NAME) .coverage .coverage.* build/ dist/ htmlcov/ *.egg-info .tox

.PHONY: venv test test-nomock test-travis coveralls fmt fmtcheck lint clean
