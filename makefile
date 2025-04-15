venv_dir = venv

run:
	python3 src/nvidiaProject.py

venv:
	pip install virtualenv
	virtualenv $(venv_dir)

activate:
	source $(venv_dir)/bin/activate
	pip install -U selenium
clean:
	rm -rf venv
