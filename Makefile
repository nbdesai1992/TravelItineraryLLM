.PHONY: env activate clean

env:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

activate:
	@echo "Run 'source venv/bin/activate' to activate the virtual environment"

clean:
	rm -rf venv
