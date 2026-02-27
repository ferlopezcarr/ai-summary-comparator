start:
	python -m src.main

venv:
	uv venv

venv-activate:
	source .venv/bin/activate

sync:
	uv sync
