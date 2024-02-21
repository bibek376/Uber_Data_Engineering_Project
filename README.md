# Uber_Data_Engineering_Project

## Installation Guide
1. Clone or Fork the Uber Taxi Data Engineering Project using SSH or HTTPS method
2. Create a Virtual Environment (optional)
3. Install dependencies like Python and Pandas package

## Project Structure 
```bash
   ├── data
   │   └── taxi_zones.csv
   ├── data_dictionary_trip_records_yellow.pdf
   ├── LICENSE
   ├── pictures
   │   └── 1.png
   ├── README.md
   ├── Uber_Data_Engineering_Project.ipynb
   └── yellow_tripdata_2023-01.csv
```

## Project Highlights
1. Real-time data
2. Data modeling
3. Open Source

## Table Of Content
1. [Project Description](#1-project-description)<br>
   - A. Problem Statement<br>
   - B. Introduction About Project<br>
   - C. Tools and Libraries
2. [Data Collection-TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) <br> <br>
    You can download all the data file used in this project by using following link, 
    ```bash
    wget -O $HOME/yello_tridata_2023-01.csv "https://shorturl.at/jpRUX"
    ```
   For taxi zone lookup dataset,
   ```bash
    wget -O $HOME/taxi_zones.csv "https://shorturl.at/oxQ46"
   ```
   Feel free to explore more dataset,
    ```bash
    wget https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/yellow
    ```

    All the data was copied from the NYC TLC [website](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

4. Generic Flow Of Project
   
   ![](https://github.com/bibek376/Uber_Data_Engineering_Project/blob/master/pictures/Project_Architecture.png)<br>
   
6. Data Development

   I am using mage-ai as ETL for data development. At first load yello trip data then filter some data (there are some string value in int column) then
   create separate csv file(after_clean.csv).

   ![](https://github.com/bibek376/Uber_Data_Engineering_Project/blob/master/pictures/etl.png)<br>

   Inside the load_clean_csv_file,
   ```python
   from mage_ai.io.file import FileIO
   if 'data_loader' not in globals():
       from mage_ai.data_preparation.decorators import data_loader
   if 'test' not in globals():
       from mage_ai.data_preparation.decorators import test
   
   import pandas as pd
   
   @data_loader
   def load_data_from_file(*args, **kwargs):
       """
       Template for loading data from filesystem.
       Load data from 1 file or multiple file directories.
   
       For multiple directories, use the following:
           FileIO().load(file_directories=['dir_1', 'dir_2'])
   
       Docs: https://docs.mage.ai/design/data-loading#fileio
       """
       df = pd.read_csv('/root/after_some_cleaning.csv')
       df=df.head(100000)
   
       return df
   
   
   @test
   def test_output(output, *args) -> None:
       """
       Template code for testing the output of the block.
       """
       assert output is not None, 'The output is undefined'


   ```
   For this project I used only 100000 records due to memory issue with mage-ai, but actual size is more than 3 million records(You can process all data if you have more than 16GB of RAM).<br>

   Inside the zone_csv_file,
   ```python
   from mage_ai.io.file import FileIO
   if 'data_loader' not in globals():
       from mage_ai.data_preparation.decorators import data_loader
   if 'test' not in globals():
       from mage_ai.data_preparation.decorators import test
   
   
   @data_loader
   def load_data_from_file(*args, **kwargs):
       """
       Template for loading data from filesystem.
       Load data from 1 file or multiple file directories.
   
       For multiple directories, use the following:
           FileIO().load(file_directories=['dir_1', 'dir_2'])
   
       Docs: https://docs.mage.ai/design/data-loading#fileio
       """
       filepath = '/root/data/taxi_zones.csv'
   
       return FileIO().load(filepath)
   
   
   @test
   def test_output(output, *args) -> None:
       """
       Template code for testing the output of the block.
       """
       assert output is not None, 'The output is undefined'

   ```

   
   
   


### 1. Project Description
#### A. Problem Statement
The TLC (Taxi and Limousine Commission) Trip Record Data provides extensive information on taxi trips in New York City, including those for yellow and green taxis. However, the sheer volume of data and redundancy pose challenges for meaningful analytics. Processing and analyzing such large datasets efficiently become crucial for extracting valuable insights and optimizing taxi services.

- **Volume and Redundancy:** The dataset is vast, containing millions of records with redundant information.
- **Data Suitability:** The raw data may not be immediately suitable for analytics due to its sheer size and unstructured nature.


#### B. Best Possible Solutions
- Big Data 
- Costly server
- ETL approach

#### C. Introduction About Project

#### D. Tools and Libraries
**Tools**<br>
- Python
- Jupyter Notebook
- PostgreSQL
- [lucid](https://lucid.app/users/login#/login)
- Mage
- GitHub

**Libraries**<br>
- Pandas
- Numpy
- Seaborn
- Matplotlib
