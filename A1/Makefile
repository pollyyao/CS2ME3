PY = python
PYFLAGS = 
DOC = doxygen
DOCFLAGS = 
DOCCONFIG = CircleDoc

SRC = src/testCircles.py

.PHONY: all prog doc clean

test: 
	$(PY) $(PYFLAGS) $(SRC)

doc: 
	$(DOC) $(DOCFLAGS) $(DOCCONFIG)
	cd latex && $(MAKE)

all: test doc

clean:
	rm -rf html
	rm -rf latex
	rm -rf CircleADT.pyc
	rm -rf Statistics.pyc