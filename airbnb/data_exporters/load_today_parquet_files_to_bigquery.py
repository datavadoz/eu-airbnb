import re

from google.cloud import bigquery

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_parquet_from_gcs_to_bigquery(blobs):
    """
    Exports blobs of parquet files into BigQuery tables.

    Args:
        blobs: A tuple that contains date string and list of blob names.
    """
    project_name = 'dtc-airbnb'
    dataset_name = 'staging'

    today_str, parquet_object_list = blobs

    bigquery_client = bigquery.Client()
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        source_format=bigquery.SourceFormat.PARQUET
    )

    # Create staging dataset if not exist
    dataset_id = f'{project_name}.{dataset_name}'
    dataset = bigquery.Dataset(dataset_id)
    bigquery_client.create_dataset(dataset, exists_ok=True, timeout=30)
    print("Created dataset {}.{}".format(bigquery_client.project, dataset.dataset_id))

    # Load parquet files into according tables
    for parquet_object in parquet_object_list:
        match = re.match(rf'{today_str}/(?P<table_name>.*)\.parquet', parquet_object)
        table_name = match.group('table_name')
        table_id = f'{dataset_id}.{table_name}'

        uri = f'gs://dtc-airbnb/{parquet_object}'
        print(f'Loading {parquet_object} into {table_id}...')

        load_job = bigquery_client.load_table_from_uri(uri, table_id, job_config=job_config)
        load_job.result()

        destination_table = bigquery_client.get_table(table_id)
        print("Loaded {} rows.".format(destination_table.num_rows))
