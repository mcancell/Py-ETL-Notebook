import os
import requests
import json
import pandas as pd
from abc import ABC, abstractmethod
from tqdm import tqdm
import zipfile  # Missing import

class DataFetcher(ABC):
    def __init__(self, url, chunk_size, where_clause):
        self.url = url
        self.chunk_size = chunk_size
        self.where_clause = where_clause

    @abstractmethod
    def fetch_data(self, offset):
        pass

class JSONDataFetcher(DataFetcher):
    def fetch_data(self, offset):
        final_url = self.url.format(self.chunk_size, offset, self.where_clause)
        response = requests.get(final_url)
        return response.json()

class CSVDataFetcher(DataFetcher):
    def fetch_data(self, offset):
        final_url = self.url.format(self.chunk_size, offset, self.where_clause)
        response = requests.get(final_url)
        return pd.read_csv(response.content)

class XLSDataFetcher(DataFetcher):
    def fetch_data(self, offset):
        final_url = self.url.format(self.chunk_size, offset, self.where_clause)
        response = requests.get(final_url)
        return pd.read_excel(response.content)

def fetch_store_data(fetcher, limit, offset, storage_dir, storage_file, compress=False, mode='w'):
    """
    Fetches data using the provided fetcher and stores it in a file.
    Parameters:
    fetcher (DataFetcher): An instance of a DataFetcher subclass.
    limit (int): The maximum number of records to fetch.
    offset (int): The starting point for fetching records.
    storage_dir (str): The directory where the file will be stored.
    storage_file (str): The name of the file to store the fetched data.
    compress (bool): Whether to compress the file into a zip file.
    mode (str): The mode to open the file, either 'w' for write or 'a' for append.
    Returns:
    None
    """
    all_data = []

    with tqdm(total=limit, desc="Fetching data", unit="record") as pbar:
        while offset < limit:
            print(f"Fetching data starting from offset: {offset}")
            data = fetcher.fetch_data(offset)
            if not data:
                print("No more data to fetch.")
                break
            all_data.extend(data)
            offset += fetcher.chunk_size
            pbar.update(len(data))
            print(f"Fetched {len(data)} records, updated offset to {offset}")

    # Create the directory if it does not exist
    os.makedirs(storage_dir, exist_ok=True)
    print(f"Storage directory '{storage_dir}' is ready.")

    # Write or append the data to a file
    file_path = os.path.join(storage_dir, storage_file)
    if mode == 'a' and os.path.exists(file_path):
        with open(file_path, mode='r') as file:
            existing_data = json.load(file)
        all_data = existing_data + all_data
        print(f"Existing data loaded from '{file_path}'.")

    # If no new data was fetched, ensure existing data is preserved
    if not all_data and mode == 'a' and os.path.exists(file_path):
        with open(file_path, mode='r') as file:
            all_data = json.load(file)
        mode = 'w'  # Change mode to 'w' to overwrite with existing data
        print("No new data fetched, preserving existing data.")

    if all_data:  # Only write to file if there is data to write
        with open(file_path, mode=mode) as file:
            json.dump(all_data, file, indent=4)
        print(f"Data written to '{file_path}'.")
        file.close()  # Ensure the file is closed before zipping

    # Compress the file if compress is True
    if compress:
        zip_path = os.path.join(storage_dir, storage_file + '.zip')
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(file_path, os.path.basename(file_path))
        os.remove(file_path)
        print(f"Data compressed to '{zip_path}'.")

    print("Data fetching and storing process completed.")
