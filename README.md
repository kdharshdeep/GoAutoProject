# GoAuto Project

## Overview
This project analyzes car sales data to optimize dealership performance in Edmonton by leveraging machine learning models, exploratory data analysis (EDA), and predictive analytics. It is designed to provide insights into geographical clusters, sales patterns, and inventory optimization.

---

## Features
- **Exploratory Data Analysis (EDA):**
  - Analyze car sales data to uncover trends and patterns.
- **Clustering:**
  - Group regions based on average price and mileage using KMeans clustering.
- **Predictive Modeling:**
  - Predict sales regions and dealership performance.
- **Interactive Visualizations:**
  - Use Streamlit to present data and insights interactively.

---

## Folder Structure
```plaintext
GoAuto Project/
├── app_files/          # Static assets for the Streamlit app
│   ├── Dealership-map.html # Map visualization
│   ├── image.png       # Logo or other static images
├── configs/            # Configuration files
│   ├── config.yaml     # YAML configuration file
├── data/               # Datasets for analysis
│   ├── CBB_Listings_LongLat.csv # Main dataset
│   ├── used_cars.csv   # Sample used cars data
│   ├── new_cars.csv    # Sample new cars data
├── docs                # Documentation
├── experiment               # Experimentation
├── model/              # Machine learning models and related code
│   ├── clustering.py   # Clustering logic (KMeans)
│   ├── prediction.py   # Prediction functions
|   ├── checkpoints
├── notebook/           # Jupyter notebooks for experimentation
│   ├── GoAuto.ipynb # Exploratory Data Analysis notebook
├── src/                # Main application logic
│   ├── app.py          # Basic Streamlit app
│   ├── advanced_app.py # Advanced Streamlit app
│   ├── data_analysis.py # Data exploration and visualization logic
│   ├── visualization.py # Visualization functions
|   ├── utilites.py
├── test/               # Unit tests for the codebase
│   ├── test_clustering.py # Tests for clustering logic
│   ├── test_prediction.py # Tests for prediction logic
├── requirements.txt    # Python dependencies
├── makefile            # Automation tasks (setup, run, test)
├── README.md           #Main Project documentation

---

## Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd GoAuto Project

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


## Usage
### Run the Basic App
```bash
streamlit run src/app.py

---

streamlit run src/advanced_app.py

