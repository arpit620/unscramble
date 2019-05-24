.PHONY: check test docs venv

check:
	@echo "Hello World...!!!"

test: 
	@echo "Testing the module...!!!"
	py.test
	cd tests && py.test
	python examples/check.py
	cd examples && python check.py

docs: 
	@echo "Preparing docs...!!!"
	cd docs && make clean html

venv:
	@echo "Testing module in virtual environment"
	rm -rf venv_test
	python3 -m venv venv_test; \
	source venv_test/bin/activate; \
	pip install .
	py.test
	cd tests && py.test test_unscramble.py
	python examples/check.py
	cd examples && python check.py
	deactivate
	rm -rf venv_test

# make data / train_model
# .PHONY: data
# data:
