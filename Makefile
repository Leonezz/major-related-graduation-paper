main: mdfile
	pandoc --filter pandoc-fignos --filter pandoc-tablenos \
		--citeproc --toc --mathjax\
		--csl chinese-gb7714-2015-numeric.csl \
		--bibliography ref.bib -M reference-section-title="参考文献" \
		-M link-citations=true --reference-doc templete.dotx \
		--resource-path="./src" \
		src/input.md -o build/output.docx

mdfile: 
	python preprocess.py