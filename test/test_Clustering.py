import pytest
from model.clustering import preprocess_used_cars
import pandas as pd

def test_preprocess_used_cars():
    data = pd.DataFrame({
        "region_label": ["A", "B"],
        "avg_price": [20000, 25000],
        "avg_mileage": [50000, 60000],
        "vin": ["1", "2"]
    })
    agg_data, scaler, kmeans = preprocess_used_cars(data)
    assert len(agg_data) == 2
    assert "cluster" in agg_data.columns
