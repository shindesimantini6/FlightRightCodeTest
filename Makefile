SOURCES=exposurejapan tests setup.py
LENGTH=96

check: $(SOURCES)
	flake8 --max-line-length=$(LENGTH) $^
	black --check --line-length $(LENGTH) $^
	pylint -E $^

black: $(SOURCES)
	black --line-length $(LENGTH) $^
