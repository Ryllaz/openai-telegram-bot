venv:
	python3 -m venv .

env:
	if [ ! -f .env ]; then cp .env.dist .env; fi

install:
	source bin/activate && pip install --no-cache-dir -r requirements.txt

up:
	source bin/activate && python3 server.py