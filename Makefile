PROJ_NAME  = video_creator
PY_CMD     = python
DOCS_DIR   = docs
SETUP      = setup.py

.PHONY: $(DOCS_DIR)

init:
	python -m pip install --upgrade pip
	if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
	if [ -f setup.py ]; then pip install -e .; fi

run:
	$(PY_CMD) -m $(PROJ_NAME)
