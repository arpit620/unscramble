 .PHONY: check test docs 

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
