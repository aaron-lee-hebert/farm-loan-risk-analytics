import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = str(os.getenv("BASE_URL"))
if BASE_URL is None:
    raise RuntimeError("BASE_URL is not set. Check your .env file.")
