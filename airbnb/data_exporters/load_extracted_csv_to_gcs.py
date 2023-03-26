import os
import shutil
from google.cloud import storage

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(*args, **kwargs):
    """
    Exports data to some source

    Args:
        args: The input variables from upstream blocks

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    if len(args) != 1:
        raise Exception('Incorrect number of arguments')

    extracted_dir = args[0]
    if not os.path.isdir(extracted_dir):
        raise FileNotFoundError(f'{extracted_dir} not exist')

    storage_client = storage.Client()
    bucket = storage_client.bucket('dtc-airbnb')

    for path, _, files in os.walk(extracted_dir):
        for file in files:
            file_path = os.path.join(path, file)
            print(f'Loading {file_path} to GCS...')
            blob = bucket.blob(file)
            blob.upload_from_filename(file_path)

    shutil.rmtree(extracted_dir)
    print(f'Deleted {extracted_dir}!')
