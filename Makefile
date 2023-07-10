.PHONY: install format lint Test Sec

install:
		poetry install

format:
		isort .
		blue . 

lint: 
		blue . --check
		isort . --check

Test:
		pytest -v
	
Sec: 	
		pip-audit
