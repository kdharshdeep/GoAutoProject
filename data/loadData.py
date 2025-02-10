#Reading the Database
#df = pd.read_csv("CBB_Listings_LongLat.csv")
import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_csv(self):
        """Loads a CSV file into a pandas DataFrame."""
        try:
            data = pd.read_csv(self.file_path)
            print(f"Data loaded successfully from {self.file_path}.")
            return data
        except Exception as e:
            print(f"Error loading data: {e}")
            return None

# Example usage
if __name__ == "__main__":
    file_path = "data/raw/CBB_Listings_LongLat.csv"
    loader = DataLoader(file_path)
    data = loader.load_csv()
    print(data.head())
