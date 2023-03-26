import datetime
import os
import shutil

from google.cloud import storage

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(input_dir):
    """
    Load transformed parquet files into Google Cloud Storage

    Args:
        input_dir: The directory contains parquet files.
    """
    if not os.path.isdir(input_dir):
        raise FileNotFoundError(f'{input_dir} not exist')

    storage_client = storage.Client()
    bucket = storage_client.bucket('dtc-airbnb')
    parent_blob = datetime.datetime.now().strftime('%Y%m%d')

    for path, _, files in os.walk(input_dir):
        parquet_files = [file for file in files if file.endswith('.parquet')]
        for parquet_file in parquet_files:
            parquet_file_path = os.path.join(path, parquet_file)
            blob_path = f'{parent_blob}/{parquet_file}'
            print(f'Loading {parquet_file_path} to {blob_path} ...')
            bucket.blob(blob_path).upload_from_filename(parquet_file_path)

    shutil.rmtree(input_dir)
    print(f'Deleted {input_dir}!')
