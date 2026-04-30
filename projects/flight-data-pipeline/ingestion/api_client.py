import requests
from config import BASE_URL

def fetch_flights():
    response = requests.get(BASE_URL)

    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code} - {response.text}")
    
    return response.json()