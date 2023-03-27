import datetime

from google.cloud import storage

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_today_parquet_files():
    """
    Load all parquet files on today from GCS.

    Returns:
        A tuple of today string and list of parquet files.
    """
    storage_client = storage.Client()
    today_str = datetime.datetime.now().strftime('%Y%m%d')
    blobs = [blob.name for blob in storage_client.list_blobs('dtc-airbnb', prefix=today_str)]
    return today_str, blobs


@test
def test_output(output) -> None:
    assert output is not None, 'The output is undefined'
