pdflatex -shell-escape asp_mining_notes.tex
bibtex8 --wolfgang asp_mining_notes
pdflatex -shell-escape asp_mining_notes.tex

evince asp_mining_notes.pdf &
