import os
import tempfile
import zipfile

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_file():
    """
    Template for loading data from filesystem.
    Load data from 1 file or multiple file directories.

    For multiple directories, use the following:
        FileIO().load(file_directories=['dir_1', 'dir_2'])

    Docs: https://docs.mage.ai/design/data-loading#fileio
    """
    project_dir = os.getenv('PROJECT_DIR')
    data_source_dir = os.path.join(project_dir, 'data-source')
    archive_zip = os.path.join(data_source_dir, 'archive.zip')
    extracted_dir = tempfile.mkdtemp()

    if not os.path.isfile(archive_zip):
        raise FileNotFoundError(f'{archive_zip} not exist!')

    with zipfile.ZipFile(archive_zip) as zip_file:
        for member in zip_file.infolist():
            extracted_file_path = os.path.join(extracted_dir, member.filename)
            print(f'Extracting {extracted_file_path}...')
            zip_file.extract(member, path=extracted_dir)

    return extracted_dir


@test
def test_output(output) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
