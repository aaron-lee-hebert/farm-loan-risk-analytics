import requests
import time
from config import BASE_URL, REQUEST_TIMEOUT, MAX_RETRIES

def fetch_flights():
    attempt = 0

    while attempt < MAX_RETRIES:
        try:
            response = requests.get(BASE_URL, timeout=REQUEST_TIMEOUT)

            if response.status_code == 200:
                return response.json()
            
            print(f"Non-200 response: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
        
        attempt += 1
        wait_time = 2 ** attempt
        print(f"Retrying in {wait_time} seconds...")
        time.sleep(wait_time)

    raise Exception("Max retries exceeded")
