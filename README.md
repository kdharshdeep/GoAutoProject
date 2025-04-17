# 🚗 GoAuto: Car Sales Analysis & Optimization

This project analyzes car sales data to optimize dealership performance in **Edmonton** using **exploratory data analysis (EDA)**, **clustering**, and **predictive modeling**. It provides actionable insights into sales trends, geographical performance via an interactive app and RESTful API.

The goal? Help dealerships make smarter, data-driven decisions on pricing, marketing, and inventory!

---

## 🔍 Key Features

- **📊 Exploratory Data Analysis (EDA):**  
  Gain insights into sales patterns, price distributions, and dealership trends.

- **🧩 Clustering Analysis:**  
  Use **KMeans** clustering to group regions based on average vehicle price and mileage.

- **🤖 Predictive Modeling:**  
  Predict sales regions and evaluate dealership performance using trained ML models.

- **📈 Interactive Visualizations:**  
  Built with **Streamlit** to allow real-time interaction and insights from the data.

- **🌐 REST API for Predictions:**  
  Flask-based API serving multiple versions of trained models for flexible integration.

---

## 📁 Project Structure

```
GoAuto Project/
├── _pycache_/
│   ├── predict_api.cpython-312.pyc
├── .dvc/
│   ├── cache/file
|   ├── tmp
│   ├── .gitignore 
├── .ytest_cache/
│   ├── v
|   ├── .gitignore
│   ├── CACHEDIR.TAG
├── .venv/
│   ├── bin
|   ├── etc
│   ├── include
├── app_files/            # Static files for the Streamlit app
│   ├── Dealership-map.html
│   └── image.png
├── configs/              # YAML config files
│   └── config.yaml
├── data/                 # Raw and processed datasets
│   ├── CBB_Listings_LongLat.csv
│   ├── used_cars.csv
│   └── new_cars.csv
├── docs/                 # Documentation
├── experiment/           # Experimental scripts or results
├── grafana/
│   ├── provisioning/
|   |    ├── dashboards/
|   |           ├──dashboard.yml
|   |           ├── predict_api_dashboard.json
│   |           ├── training_dashboard.json 
│   |    ├──datasources/
|   |            ├── prometheus.yml
├── logs/
│   ├── api.log
|   ├── train.log
├── mlartifacts
├── mlflow-data
├── mlruns
├── model/                # Model training, prediction, and clustering logic
│   ├── clustering.py
│   ├── prediction.py
│   ├── checkpoints/
│   ├── __init__.py
│   └── train.py
├── notebook/             # Jupyter notebooks for EDA and experimentation
│   └── GoAuto.ipynb
├── prometheus/
|   ├── rules
|   ├── prometheus.yml
├── src/                  # Main application logic
│   ├── app.py
│   ├── advanced_app.py
│   ├── data_analysis.py
│   ├── visualization.py
│   └── utilities.py
├── test/                 # Unit tests
│   ├── test_clustering.py
│   └── test_prediction.py
├── .dockerignore
├── docker-compose.yml
├── Dockerfile
├── Dockerfile.mlflow
├── makefile 
├── predict_api.py             # Automation for setup and tasks
└── README.md             # Project overview and instructions
├── requirements.txt      # Python dependencies
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd GoAuto\ Project
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

### Run the Basic Streamlit App
```bash
streamlit run src/app.py
```

### Run the Advanced Streamlit App
```bash
streamlit run src/advanced_app.py
```

---

## 🔌 API Endpoints

### 1️⃣ API Overview

The **GoAuto Flask API** serves KMeans clustering models to predict the best **sales region** for a car based on **price** and **mileage**. It includes:

- Multiple prediction endpoints (V1 & V2 models)
- Health check and root endpoints

---

### 2️⃣ Available Endpoints

| **Method** | **Endpoint**     | **Description**                                 |
|------------|------------------|-------------------------------------------------|
| `GET`      | `/health_status` | API health check                                |
| `GET`      | `/`              | Welcome message with usage instructions         |
| `POST`     | `/v1/predict`    | Predict region using **Model V1 (6 clusters)**  |
| `POST`     | `/v2/predict`    | Predict region using **Model V2 (8 clusters)**  |

---

### 3️⃣ Example: Check API Health
```bash
curl -X GET http://127.0.0.1:9999/health_status
```

---

## 🐳 Run with Docker

To build and run the app and API using Docker:

```bash
docker-compose up -d --build
```

---

## 📝 Final Notes

- This project is optimized for analyzing **Edmonton-based dealership data**, but can be adapted to other locations.
- Clustering models can be retrained with custom configurations.
- Make sure to review and customize the `config.yaml` file as needed for deployments.