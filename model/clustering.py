import yaml
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

# Load configuration
with open("configs/config.yaml", "r") as f:
    config = yaml.safe_load(f)

data_path = config["paths"]["data"]

class ClusteringModel:
    def __init__(self, n_clusters=6, random_state=42):
        """
        Initializes the ClusteringModel with specified parameters.
        """
        self.n_clusters = n_clusters
        self.random_state = random_state
        self.model = None
        self.scaler = MinMaxScaler()

    def train(self, data, columns_to_scale):
        """
        Trains the KMeans model on the given data.
        
        Parameters:
        - data: Pandas DataFrame with input data.
        - columns_to_scale: List of column names to scale and use for clustering.
        
        Returns:
        - DataFrame with cluster labels added as a new column.
        """
        # Scale the data
        scaled_data = self.scaler.fit_transform(data[columns_to_scale])
        
        # Train the KMeans model
        self.model = KMeans(n_clusters=self.n_clusters, random_state=self.random_state).fit(scaled_data)
        
        # Assign clusters
        data["cluster"] = self.model.labels_
        print(f"Model trained with {self.n_clusters} clusters.")
        return data

    def predict(self, new_data, columns_to_scale):
        """
        Predicts the cluster for new data using the trained model.
        
        Parameters:
        - new_data: Pandas DataFrame with input data.
        - columns_to_scale: List of column names to scale and use for prediction.
        
        Returns:
        - Array of cluster predictions.
        """
        if self.model is None:
            raise ValueError("Model has not been trained yet.")
        
        scaled_data = self.scaler.transform(new_data[columns_to_scale])
        return self.model.predict(scaled_data)

# Example usage
if __name__ == "__main__":
    # Load dataset
    df = pd.read_csv(f"{data_path}CBB_Listings_LongLat.csv")
    print("Data loaded successfully:", df.shape)

    # Initialize ClusteringModel
    clustering = ClusteringModel(n_clusters=config["clustering"]["n_clusters"], random_state=config["clustering"]["random_state"])
    
    # Train the model
    if "avg_price" in df.columns and "avg_mileage" in df.columns:
        df = clustering.train(df, ["avg_price", "avg_mileage"])
        print(df.head())
    else:
        print("Required columns 'avg_price' and 'avg_mileage' not found in the dataset.")
