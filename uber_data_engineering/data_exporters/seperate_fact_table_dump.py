import os 
from mage_ai.io.file import FileIO
from pandas import DataFrame

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_file(data, **kwargs) -> None:
    """
    Template for exporting data to filesystem.

    Docs: https://docs.mage.ai/design/data-loading#fileio
    """
    output_dir='/home/bibek/Desktop/uber_data_engineering/data'
    for name,df in data:
        


    filepath = 'path/to/write/dataframe/to.csv'
    FileIO().export(df, filepath)
