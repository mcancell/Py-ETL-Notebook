import os
import requests
import json
from tqdm import tqdm
import zipfile
import time

class JSONDataFetcher:
    def __init__(self, url, chunk_size, where_clause):
        self.url = url
        self.chunk_size = chunk_size
        self.where_clause = where_clause

    def fetch_data(self, offset):
        final_url = self.url.format(self.chunk_size, offset, self.where_clause)
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(final_url, headers=headers, timeout=10)
        return response.json()

def fetch_store_data(fetcher, limit, offset, storage_dir, storage_file, compress=False, mode='w', pause_duration=5, max_reinitialize_offset=10000):
    """
    Fetches data using the provided fetcher and stores it in a file.
    Parameters:
    fetcher (JSONDataFetcher): An instance of JSONDataFetcher.
    limit (int): The maximum number of records to fetch.
    offset (int): The starting point for fetching records.
    storage_dir (str): The directory where the file will be stored.
    storage_file (str): The name of the file to store the fetched data.
    compress (bool): Whether to compress the file into a zip file.
    mode (str): The mode to open the file, either 'w' for write or 'a' for append.
    pause_duration (int): The duration to pause before retrying the connection.
    max_reinitialize_offset (int): The maximum offset after which the fetcher will be reinitialized.
    Returns:
    None
    """
    all_data = []
    
    max_offset = 0  # Initialize max_offset
    consecutive_no_data_attempts = 0  # Track consecutive attempts with no data
    max_no_data_attempts = 5  # Maximum allowed consecutive attempts with no data

    with tqdm(total=limit, desc="Fetching data", unit="record") as pbar:
        while offset < limit and consecutive_no_data_attempts < max_no_data_attempts:
            try:
                #print(f"Fetching data starting from offset: {offset}")
                data = fetcher.fetch_data(offset)
                if not data or len(data) < fetcher.chunk_size:
                    consecutive_no_data_attempts += 1
                    print(f"No more data to fetch, attempt {consecutive_no_data_attempts}/{max_no_data_attempts}.")
                    if consecutive_no_data_attempts >= max_no_data_attempts:
                        print("Maximum consecutive no data attempts reached, stopping fetch process.")
                        break
                    time.sleep(pause_duration)  # Add delay before retrying
                    continue
                consecutive_no_data_attempts = 0  # Reset counter on successful fetch
                all_data.extend(data)
                offset += fetcher.chunk_size
                max_offset += fetcher.chunk_size  # Increment max_offset
                pbar.update(len(data))
                #print(f"Fetched {len(data)} records, updated offset to {offset}")
                if max_offset >= max_reinitialize_offset:
                    print("Max reinitialize offset reached. Reinitializing fetcher.")
                    time.sleep(pause_duration)  # Add delay before reinitializing
                    max_offset = 0  # Reset max_offset
                    fetcher = JSONDataFetcher(fetcher.url, fetcher.chunk_size, fetcher.where_clause)  # Reinitialize fetcher
            except requests.exceptions.RequestException as e:
                print(f"Error fetching data: {e}")
                print(f"Retrying after {pause_duration} seconds...")
                time.sleep(pause_duration)

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
        print(f"Compressing file '{file_path}' to '{zip_path}'")
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(file_path, os.path.basename(file_path))
        os.remove(file_path)
        print(f"Data compressed to '{zip_path}'.")

    print("Data fetching and storing process completed.")
