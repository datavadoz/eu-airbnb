import os

import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


def clean_airbnb_csv_data(csv_file_path: str) -> pd.DataFrame:
    """
    Clean Airbnb price data in a csv file with following data type:
    =================================
    realSum                     float
    room_type                   str
    room_shared                 bool
    room_private                bool
    person_capacity             int
    host_is_superhost           bool
    multi                       bool
    biz                         bool
    cleanliness_rating          int
    guest_satisfaction_overall  int
    bedrooms                    int
    dist                        float
    metro_dist                  float
    lng                         float
    lat                         float
    =================================

    Args:
        csv_file_path: Path of a CSV file.

    Returns:
        A cleaned dataframe
    """
    schema = {
        'realSum': float,
        'room_type': str,
        'room_shared': bool,
        'room_private': bool,
        'person_capacity': int,
        'host_is_superhost': bool,
        'multi': bool,
        'biz': bool,
        'cleanliness_rating': int,
        'guest_satisfaction_overall': int,
        'bedrooms': int,
        'dist': float,
        'metro_dist': float,
        'lng': float,
        'lat': float
    }
    df = pd.read_csv(csv_file_path).astype(schema)
    df = df[schema.keys()]
    return df


@transformer
def transform(input_dir):
    """
    Transform Airbnb price data from CSV files in input_dir into parquet files.

    Args:
        input_dir: The directory contains CSV files.

    Returns:
        Temporary directory path that consists of transformed parquet files
    """

    if not os.path.isdir(input_dir):
        raise FileNotFoundError(f'{input_dir} not exist')

    for path, _, files in os.walk(input_dir):
        csv_files = [file for file in files if file.endswith('.csv')]
        for csv_file in csv_files:
            csv_file_path = os.path.join(path, csv_file)
            parquet_file_path = csv_file_path.replace('.csv', '.parquet')
            df = clean_airbnb_csv_data(csv_file_path)
            df.to_parquet(parquet_file_path)

    return input_dir


@test
def test_output(output) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
