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
    after_filtered_df=data[data['VendorID'] != 'VendorID']
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

    #prepare data for zones_dim table i.e. data_2
    zones_dim=data_2

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

    data_frame_list=[vendor_dim,payment_dim,rate_dim,store_and_forward_dim,
                    zones_dim,date_time_dim]
    
    data_frame_dict={
        'vendor_dim':vendor_dim,
        'payment_dim':payment_dim,
        'rate_dim':rate_dim,
        'store_and_forward_dim':store_and_forward_dim,
        'zones_dim':zones_dim,
        'date_time_dim':date_time_dim
    }

    return data_frame_dict


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
