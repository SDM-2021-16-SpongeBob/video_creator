PROJ_NAME  = video_creator
PY_CMD     = python
DOCS_DIR   = docs
SETUP      = setup.py

.PHONY: $(DOCS_DIR)

init:
	pip install -r requirements.txt

run:
	$(PY_CMD) -m $(PROJ_NAME)
