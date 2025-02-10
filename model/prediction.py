import numpy as np

def predict_used_car_region(price, mileage, scaler, kmeans, agg_data):
    car_features = np.array([[price, mileage]])
    car_features_scaled = scaler.transform(car_features)
    car_features_scaled[:, 1] *= 1.5
    predicted_cluster = kmeans.predict(car_features_scaled)[0]
    return agg_data[agg_data["cluster"] == predicted_cluster][["region_label", "total_sales"]]

def predict_new_car_region(price, drivetrain, scaler, kmeans, agg_data, encoder):
    drivetrain_encoded = encoder.transform([[drivetrain]])
    car_features = np.array([[price] + list(drivetrain_encoded[0])])
    car_features_scaled = scaler.transform(car_features)
    predicted_cluster = kmeans.predict(car_features_scaled)[0]
    return agg_data[agg_data["cluster"] == predicted_cluster][["region_label", "total_sales"]]
