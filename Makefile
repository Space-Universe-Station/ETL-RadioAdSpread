# Define virtual environment name
VENV = radadspdenv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

# Create a virtual environment and Install dependencies
venv: requirements.txt
	@echo "Installing python packages..."
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt


clean:
	rm -rf __pycache

# Default target: create the virtual environment, activate it, install dependencies
default: clean venv 
