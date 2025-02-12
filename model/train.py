import os
import yaml
import pandas as pd
import joblib
from model.clustering import ClusteringModel

# Load YAML configuration
with open("configs/config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Get correct data paths from YAML config
data_path = config["paths"]["app_files"]  # Use `app_files/` instead of `data/`

# Load datasets
df_used = pd.read_csv(f"{data_path}/used_cars.csv")
df_new = pd.read_csv(f"{data_path}/new_cars.csv")

# Add a column to distinguish used vs. new cars
df_used["car_type"] = "Used"
df_new["car_type"] = "New"

# Combine both datasets
df = pd.concat([df_used, df_new], ignore_index=True)

# Rename columns to match expected format
df.rename(columns={"price": "avg_price"}, inplace=True)

# Ensure required columns exist
if "avg_price" not in df.columns or "mileage" not in df.columns:
    raise ValueError(f"Error: Required columns not found. Available columns: {df.columns}")

# Initialize the clustering model
clustering = ClusteringModel(n_clusters=config["clustering"]["n_clusters"], random_state=config["clustering"]["random_state"])

# Train the model
df = clustering.train(df, ["avg_price", "mileage"])  # Use corrected column names

# ✅ Ensure `checkpoints/` directory exists before saving models
os.makedirs("model/checkpoints", exist_ok=True)

# Save the trained model and scaler
joblib.dump(clustering.model, "model/checkpoints/kmeans_model.pkl")
joblib.dump(clustering.scaler, "model/checkpoints/scaler.pkl")

print("✅ Model training completed and saved successfully!")
