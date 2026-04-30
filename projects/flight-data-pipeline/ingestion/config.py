import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = str(os.getenv("BASE_URL"))
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 10))
MAX_RETRIES = int(os.getenv("MAX_RETRIES", 3))
OUTPUT_DIR = str(os.getenv("OUTPUT_DIR", "data/bronze"))
