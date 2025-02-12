# Create virtual environment
setup:
	python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

# Install dependencies
install:
	source venv/bin/activate && pip install -r requirements.txt

# Run basic app
run-basic:
	source venv/bin/activate && streamlit run src/app.py

# Run advanced app
run-advanced:
	source venv/bin/activate && streamlit run src/advanced_app.py

# Run tests inside virtual environment
test:
	source venv/bin/activate && PYTHONPATH=$(pwd) pytest test/

# Clean up temporary files
clean:
	rm -rf __pycache__ */__pycache__
