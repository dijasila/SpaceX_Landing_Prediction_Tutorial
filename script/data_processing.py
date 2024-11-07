import pandas as pd
import json

def load_data(filepath='../data/spacex_data.json'):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return pd.DataFrame(data)

def clean_data(df):
    # Example cleaning steps
    df = df.dropna(subset=['flight_number', 'launch_date_utc'])
    df['launch_date_utc'] = pd.to_datetime(df['launch_date_utc'])
    return df