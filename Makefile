PROJ_NAME  = video_creator
PY_CMD     = python
DOCS_DIR   = docs
SETUP      = setup.py

.PHONY: $(DOCS_DIR) clean clean-pyc clean-build

init:
	python -m pip install --upgrade pip
	if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
	if [ -f setup.py ]; then pip install -e .; fi

run:
	$(PY_CMD) -m $(PROJ_NAME)

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
