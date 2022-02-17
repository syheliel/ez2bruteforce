package := ez2bruteforce
sources := $(wildcard $(package)/*.py)

stub: $(sources)
	stubgen --output . --package src.$(package)

dist: setup.py stub
	python $< sdist bdist_wheel

publish: dist
	twine upload dist/*

.PHONY += stub dist publish