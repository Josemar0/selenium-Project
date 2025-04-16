venv_dir = venv

run:venv/bin/activate
	./$(venv_dir)/bin/python3 src/nvidiaProject.py

venv/bin/activate:requirements.txt
	python3 -m venv $(venv_dir)
	@echo -e "Creating virtual environment...\n"
	./$(venv_dir)/bin/pip install -r requirements.txt
	
clean:
	rm -rf __pycache__
	rm -rf venv
