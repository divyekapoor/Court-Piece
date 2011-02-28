all: test coverage
	
coverage: test
	@echo -----------------------------------------
	@echo      Coverage Reports
	@echo -----------------------------------------
	python coverage.py .coverage -r card.py

test: card.py card_tests.py card_tests.pyc
	@echo ------------------------------------------
	@echo      Tests
	@echo ------------------------------------------
	python coverage.py .coverage -x ./card_tests.py

	
clean:
	rm *,cover *.pyc *.pyo
	
.PHONY: all test coverage clean
