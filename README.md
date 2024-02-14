# Uber_Data_Engineering_Project

## Installation Guide
1. Clone or Fork the Uber Taxi Data Engineering Project using SSH or HTTPS method
2. Create a Virtual Environment (optional)
3. Install dependencies like Python and Pandas package

## Project Highlights
1. Real-time data
2. Data modeling
3. Open Source

## Table Of Content
1. [Project Description](#1-project-description)<br>
   - A. Problem Statement<br>
   - B. Introduction About Project<br>
   - C. Tools and Libraries
2. [Data Collection-TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) <br>
    ```bash
    wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet
    ```
    Since the latest data is in parquet format, you can convert parquet data into CSV data using [tablab](https://www.tablab.app/convert/parquet/csv) or use an external resource from Data Engineering Zoomcamp. <br>
    ```bash
    wget https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/yellow
    ```
    In this project i am using one more data file: taxi zone lookup which is useful to detemine pickup location and dropoff location.
   ```bash
       wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet
   ```
    All the data was copied from the NYC TLC [website](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

4. Generic Flow Of Project
5. Data Deployment


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
