# Create virtual environment
setup:
	python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

# Install dependencies
install:
	pip install -r requirements.txt

# Run basic app
run-basic:
	streamlit run src/app.py

# Run advanced app
run-advanced:
	streamlit run src/advanced_app.py

# Run tests
test:
	pytest test/

# Clean up temporary files
clean:
	rm -rf __pycache__ */__pycache__
