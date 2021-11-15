

.PHONY: $(DOCS_DIR) clean clean-pyc clean-build

init:
	python -m pip install --upgrade pip
	if [ -f $(PKG_LIST) ]; then pip install -r $(PKG_LIST); fi
	if [ -f $(SETUP) ]; then pip install -e .; fi

run:
	$(PY_CMD) -m $(PROJ_NAME) -h

build:
	$(PY_CMD) $(SETUP) sdist

lint:
	$(PY_CMD) -m $(LINT_CMD) $(PROJ_NAME)

clean-pyc:
	@find . -name '*.pyc' -delete
	@find . -name '__pycache__' -type d | xargs rm -fr
	@find . -name '.pytest_cache' -type d | xargs rm -fr

clean-build:
	@rm --force --recursive build/
	@rm --force --recursive dist/
	@rm --force --recursive *.egg-info

clean: clean-pyc clean-build
	@echo "## Clean all data."
