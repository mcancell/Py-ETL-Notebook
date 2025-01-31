import pandas as pd
import polars as pl

class DataLoader:
    """
    DataLoader is a class for loading data from various file formats into either pandas or polars DataFrames.
    Attributes:
        datasource (str): The path to the data source file.
        frametype (str): The type of DataFrame to load the data into ('pandas' or 'polars').
        is_compressed (bool): Indicates whether the data source file is compressed.
    Methods:
        load_data():
            Loads data from the datasource into the specified DataFrame type.
        _load_to_pandas():
            Loads data from the datasource into a pandas DataFrame.
        _load_to_polars():
            Loads data from the datasource into a polars DataFrame.
    Raises:
        ValueError: If an unsupported frame type or file type is provided.
    Author:
        Mike Cancell via CoPilot
    """
    def __init__(self, datasource, frametype, is_compressed=False):
        self.datasource = datasource
        self.frametype = frametype.lower()
        self.is_compressed = is_compressed

    def load_data(self):
        if self.frametype == 'pandas':
            return self._load_to_pandas()
        elif self.frametype == 'polars':
            return self._load_to_polars()
        else:
            raise ValueError(f"Unsupported frame type: {self.frametype}")

    def _load_to_pandas(self):
        if self.datasource.endswith('.csv'):
            return pd.read_csv(self.datasource, compression='infer' if self.is_compressed else None)
        elif self.datasource.endswith('.json'):
            return pd.read_json(self.datasource, compression='infer' if self.is_compressed else None)
        elif self.datasource.endswith('.parquet'):
            return pd.read_parquet(self.datasource)
        else:
            raise ValueError(f"Unsupported file type for pandas: {self.datasource}")

    def _load_to_polars(self):
        if self.datasource.endswith('.csv'):
            return pl.read_csv(self.datasource)
        elif self.datasource.endswith('.json'):
            return pl.read_json(self.datasource)
        elif self.datasource.endswith('.parquet'):
            return pl.read_parquet(self.datasource)
        else:
            raise ValueError(f"Unsupported file type for polars: {self.datasource}")

# Example usage:
# loader = DataLoader('data.csv.gz', 'pandas', is_compressed=True)
# df = loader.load_data()