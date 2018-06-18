PY = python
PYFLAGS = 
DOC = doxygen
DOCFLAGS = 
DOCCONFIG = doxConfig

SRC = src/testCircleDeque.py

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
	rm -rf circleADT.pyc
	rm -rf deque.pyc
	rm -rf lineADT.pyc
	rm -rf pointADT.pyc