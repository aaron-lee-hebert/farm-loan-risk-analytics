import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = str(os.getenv("BASE_URL"))
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 10))
MAX_RETRIES = int(os.getenv("MAX_RETRIES", 3))
OUTPUT_DIR = str(os.getenv("OUTPUT_DIR", "data/bronze"))
AZURE_STORAGE_ACCOUNT = os.getenv("AZURE_STORAGE_ACCOUNT")
AZURE_STORAGE_KEY = os.getenv("AZURE_STORAGE_KEY")
AZURE_CONTAINER_BRONZE = os.getenv("AZURE_CONTAINER_BRONZE", "bronze")
