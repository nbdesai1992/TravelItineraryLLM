.PHONY: env

env:
	py -m venv venv
	venv\Scripts\activate && pip install -r requirements.txt