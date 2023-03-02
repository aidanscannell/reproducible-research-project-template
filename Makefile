.PHONY: run clean paper

FILENAME=main
PAPER_DIR=paper
AUX_DIR=.aux

VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

media: $(VENV)/bin/activate
	$(PYTHON) src/figures.py --save_dir="./${PAPER_DIR}/figs"
	$(PYTHON) src/tables.py --save_dir="./${PAPER_DIR}/tables"

all: $(VENV)/bin/activate
	$(PYTHON) src/train.py
	$(PYTHON) src/figures.py --save_dir="./${PAPER_DIR}/figs"
	$(PYTHON) src/tables.py --save_dir="./${PAPER_DIR}/tables"

run: $(VENV)/bin/activate
	$(PYTHON) src/train.py

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

figures: $(VENV)/bin/activate
	$(PYTHON) src/figures.py --save_dir="./${PAPER_DIR}/figs"

tables: $(VENV)/bin/activate
	$(PYTHON) src/tables.py --save_dir="./${PAPER_DIR}/tables"

clean:
	rm -rf __pycache__
	rm -rf $(VENV)

clean:
	trash ${AUX_DIR}

submission:
	gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER -dPrinted=false -dFirstPage=1 -dLastPage=13 -sOutputFile=submission.pdf ${FILENAME}.pdf

appendix:
	gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER -dPrinted=false -dFirstPage=14 -sOutputFile=supplement.pdf ${FILENAME}.pdf


# # paper: ${PAPER_DIR}/${FILENAME}.tex
# paper: figures tables
# 	cd paper && latexmk -pdf -interaction=nonstopmode -auxdir=${AUX_DIR} -outdir=${AUX_DIR} ${FILENAME}.tex
# 	# cd paper && mv ${AUX_DIR}/${FILENAME}.pdf ${FILENAME}.pdf
# media: $(VENV)/bin/activate
# 	$(PYTHON) src/figures.py --save_dir="./paper/fig"
# 	$(PYTHON) src/tables.py --save_dir="./paper/tables"
# 	# latexmk -pdf -interaction=nonstopmode -auxdir=${PAPER_DIR}/${AUX_DIR} -outdir=${PAPER_DIR}/${AUX_DIR} ${PAPER_DIR}/${FILENAME}.tex
# 	# mv ${PAPER_DIR}/${AUX_DIR}/${FILENAME}.pdf ${PAPER_DIR}/${FILENAME}.pdf
