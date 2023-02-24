# .PHONY: run clean figures tables
.PHONY: run clean

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

all:
	$(PYTHON) src/plot.py --save_dir="./figures"
	$(PYTHON) src/plot.py --save_dir="./tables"

run: $(VENV)/bin/activate
	$(PYTHON) src/train.py

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

figures: $(VENV)/bin/activate
	$(PYTHON) src/plot.py --save_dir="./figures"

tables: $(VENV)/bin/activate
	$(PYTHON) src/plot.py --save_dir="./tables"

clean:
	rm -rf __pycache__
	rm -rf $(VENV)
