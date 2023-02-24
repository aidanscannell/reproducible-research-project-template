filename=main
aux_dir=.aux

paper:
	latexmk -pdf -interaction=nonstopmode -auxdir=${aux_dir} -outdir=${aux_dir} ${filename}.tex
	mv ${aux_dir}/${filename}.pdf ${filename}.pdf

clean:
	trash ${aux_dir}

submission:
	gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER -dPrinted=false -dFirstPage=1 -dLastPage=13 -sOutputFile=submission.pdf ${filename}.pdf

appendix:
	gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER -dPrinted=false -dFirstPage=14 -sOutputFile=supplement.pdf ${filename}.pdf
