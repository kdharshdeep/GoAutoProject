import numpy as np
import joblib
import pandas as pd

# Load trained model and scaler
kmeans = joblib.load("model/checkpoints/kmeans_model.pkl")
scaler = joblib.load("model/checkpoints/scaler.pkl")

# Sample aggregated data (replace with actual dataset if needed)
agg_data = pd.DataFrame({
    "region_label": ["Region1", "Region2", "Region3"],
    "total_sales": [500, 600, 700],
    "cluster": [0, 1, 2]  # Example cluster labels
})

def predict_used_car_region(price, mileage):
    """Predicts which region a used car will be sold in."""
    car_features = pd.DataFrame([[price, mileage]], columns=["avg_price", "mileage"])  # Convert to DataFrame
    car_features_scaled = scaler.transform(car_features)  
    car_features_scaled[:, 1] *= 1.5  # Adjust mileage weighting
    predicted_cluster = kmeans.predict(car_features_scaled)[0]

    return agg_data[agg_data["cluster"] == predicted_cluster][["region_label", "total_sales"]]

# Example usage
if __name__ == "__main__":
    print("🔎 Running Used Car Prediction...")
    result = predict_used_car_region(25000, 60000)
    print(result)
