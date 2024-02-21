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
   Inside the fact_and_dimension_table,<br>
   ```python
   import pandas as pd
   if 'transformer' not in globals():
       from mage_ai.data_preparation.decorators import transformer
   if 'test' not in globals():
       from mage_ai.data_preparation.decorators import test
   
   
   @transformer
   def transform(data,data_2, *args, **kwargs):
       """
       Template code for a transformer block.
   
       Add more parameters to this function if this block has multiple parent blocks.
       There should be one parameter for each output variable from each parent block.
   
       Args:
           data: The output from the upstream parent block
           args: The output from any additional upstream blocks (if applicable)
   
       Returns:
           Anything (e.g. data frame, dictionary, array, int, str, etc.)
       """
       # Specify your transformation logic here
       after_filtered_df=data_2
       after_filtered_df=after_filtered_df[after_filtered_df['VendorID'] != 'VendorID']
       after_filtered_df['VendorID']=pd.to_numeric(after_filtered_df['VendorID'],downcast='integer')
       after_filtered_df['tpep_pickup_datetime']=pd.to_datetime(after_filtered_df['tpep_pickup_datetime'])
       after_filtered_df['tpep_dropoff_datetime']=pd.to_datetime(after_filtered_df['tpep_dropoff_datetime'])
       after_filtered_df['passenger_count']=pd.to_numeric(after_filtered_df['passenger_count'],downcast='integer')
       after_filtered_df['trip_distance']=pd.to_numeric(after_filtered_df['trip_distance'])
       after_filtered_df['RatecodeID']=pd.to_numeric(after_filtered_df['RatecodeID'],downcast='integer')
       #after_filtered_df['store_and_fwd_flag']=pd.to_numeric(after_filtered_df['store_and_fwd_flag'])
       after_filtered_df['PULocationID']=pd.to_numeric(after_filtered_df['PULocationID'])
       after_filtered_df['DOLocationID']=pd.to_numeric(after_filtered_df['DOLocationID'])
       after_filtered_df['payment_type']=pd.to_numeric(after_filtered_df['payment_type'],downcast='integer')  
       after_filtered_df['fare_amount']=pd.to_numeric(after_filtered_df['fare_amount'])
       after_filtered_df['extra']=pd.to_numeric(after_filtered_df['extra'])
       after_filtered_df['mta_tax']=pd.to_numeric(after_filtered_df['mta_tax'])
       after_filtered_df['tip_amount']=pd.to_numeric(after_filtered_df['tip_amount'])
       after_filtered_df['tolls_amount']=pd.to_numeric(after_filtered_df['tolls_amount'])
       after_filtered_df['improvement_surcharge']=pd.to_numeric(after_filtered_df['improvement_surcharge'])
       after_filtered_df['total_amount']=pd.to_numeric(after_filtered_df['total_amount'])
       after_filtered_df['congestion_surcharge']=pd.to_numeric(after_filtered_df['congestion_surcharge'])
       after_filtered_df['airport_fee']=pd.to_numeric(after_filtered_df['airport_fee'])
       
       #For date and time
       after_filtered_df['pickup_year'] = after_filtered_df['tpep_pickup_datetime'].dt.year
       after_filtered_df['pickup_month'] = after_filtered_df['tpep_pickup_datetime'].dt.month
       after_filtered_df['pickup_day'] = after_filtered_df['tpep_pickup_datetime'].dt.day
       after_filtered_df['pickup_weekday'] = after_filtered_df['tpep_pickup_datetime'].dt.weekday
       after_filtered_df['pickup_hour'] = after_filtered_df['tpep_pickup_datetime'].dt.hour
       after_filtered_df['dropoff_year'] = after_filtered_df['tpep_dropoff_datetime'].dt.year
       after_filtered_df['dropoff_month'] = after_filtered_df['tpep_dropoff_datetime'].dt.month
       after_filtered_df['dropoff_day'] = after_filtered_df['tpep_dropoff_datetime'].dt.day
       after_filtered_df['dropoff_weekday'] = after_filtered_df['tpep_dropoff_datetime'].dt.weekday
       after_filtered_df['dropoff_hour'] = after_filtered_df['tpep_dropoff_datetime'].dt.hour
       
       #if tpep_pickup_datetime and tpep_dropoff_datetime is same logically it is not possible
       after_duplicate_filtered_df=after_filtered_df['tpep_pickup_datetime'] != after_filtered_df['tpep_dropoff_datetime']
       after_duplicate_filtered_df = after_filtered_df[after_duplicate_filtered_df]
   
       after_duplicate_filtered_df['id'] = after_duplicate_filtered_df.index+1
       date_time_dim=after_duplicate_filtered_df[['id','tpep_pickup_datetime','pickup_year','pickup_month',
                  'pickup_day','pickup_weekday','pickup_hour','tpep_dropoff_datetime',
                 'dropoff_year','dropoff_month','dropoff_day','dropoff_weekday','dropoff_hour']]
   
       #prepare data for vendor_dim table
       vendor_mode_data={'vendor_id':[1,2],
                     'vendor_description':["Creative Mobile Technologies, LLC","VeriFone Inc."]
                       }
       vendor_dim=pd.DataFrame(vendor_mode_data)
   
       #prepare data for payment_dim table
       payment_dim_data={'payment_id':[1,2,3,4,5,6],
                     'payment_description':["Credit card, LLC","Cash","No charge","Dispute","Unknown","Voided trip"]
                   }
       payment_dim=pd.DataFrame(payment_dim_data)
   
   
       #prepare data for rate_dim table
       rate_dim_data={'rate_id':[1,2,3,4,5,6],
                     'rate_description':["Standard rate","JFK","Newark","Nassau or Westchester",
                                            "Negotiated fare","Group ride"]
                       }
       rate_dim=pd.DataFrame(rate_dim_data)
   
       #prepare data for zones_dim table i.e. data
       zones_dim=data
   
       #prepare data for store_and_forward_dim table
       store_and_forward_dim_data={'store_and_forward_id':[1,2],
                     'store_and_forward_flag':["Y","N"],
                     'store_and_forward_description':["store and forward trip","not a store and forward trip"]
                       }
       store_and_forward_dim=pd.DataFrame(store_and_forward_dim_data)
   
       #prepare data for vendor_dim table
       after_duplicate_filtered_df_data={
                       "Y":1,
                       "N":2}
   
       after_duplicate_filtered_df['store_and_fwd_flag']=after_duplicate_filtered_df['store_and_fwd_flag'].map(after_duplicate_filtered_df_data)
       
       after_duplicate_filtered_df_and_rename=after_duplicate_filtered_df.rename(columns={'VendorID': 'vendor_id',
                                       'PULocationID': 'pu_location_id',
                                       'DOLocationID': 'do_location_id',
                                       'store_and_fwd_flag': 'store_and_forward_id',
                                       'RatecodeID': 'rate_id',
                                       'payment_type': 'payment_id'
                                       })
   
       after_duplicate_filtered_df_and_rename['id'] = after_duplicate_filtered_df.index+1
       after_duplicate_filtered_df_and_rename['date_time_id'] = after_duplicate_filtered_df.index+1
   
       fact_table=after_duplicate_filtered_df_and_rename[['id','vendor_id','date_time_id','pu_location_id',
                                          'do_location_id','store_and_forward_id',
                                          'payment_id','rate_id','passenger_count',
                                          'trip_distance','fare_amount','extra','mta_tax',
                                          'tip_amount','tolls_amount','improvement_surcharge',
                                          'total_amount','congestion_surcharge','airport_fee'
                                          ]]
   
   
       data_frame_list=[vendor_dim,payment_dim,rate_dim,store_and_forward_dim,
                       zones_dim,date_time_dim,fact_table]
       
       data_frame_dict={
           'vendor_dim':vendor_dim,
           'payment_dim':payment_dim,
           'rate_dim':rate_dim,
           'store_and_forward_dim':store_and_forward_dim,
           'zones_dim':zones_dim,
           'date_time_dim':date_time_dim,
           'fact_table':fact_table
       }
   
       return data_frame_dict
   
   
   @test
   def test_output(output, *args) -> None:
       """
       Template code for testing the output of the block.
       """
       assert output is not None, 'The output is undefined'
   ```
   
   This is the heart of the project where seven different dataframe has been created using ER diagram.
   
   


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
