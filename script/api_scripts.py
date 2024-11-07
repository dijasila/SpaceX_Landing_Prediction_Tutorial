import requests
import json

def fetch_spacex_data(endpoint="https://api.spacexdata.com/v4/launches"):
    response = requests.get(endpoint)
    if response.status_code == 200:
        data = response.json()
        with open('../data/spacex_data.json', 'w') as f:
            json.dump(data, f)
        return data
    else:
        print("Failed to retrieve data.")
        return None