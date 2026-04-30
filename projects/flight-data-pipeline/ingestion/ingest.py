import json
from datetime import datetime, timezone
from api_client import fetch_flights
from azure_client import AzureClient
from config import AZURE_CONTAINER_BRONZE
from logger import logger


def main():
    logger.info("Starting ingestion job")

    try:
        data = fetch_flights()
        azure = AzureClient()

        now = datetime.now(timezone.utc)
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        blob_path = f"year={now.year}/month={now.month:02}/day={now.day:02}/flights_{timestamp}.json"

        wrapped_data = {
            "ingestion_time": timestamp,
            "source": "opensky",
            "data": data
        }

        azure.upload_json(
            container=AZURE_CONTAINER_BRONZE,
            file_path=blob_path,
            data=json.dumps(wrapped_data)
        )

        print(f"Uploaded to Azure: {blob_path}")
    except Exception as e:
        logger.error(f"Ingestion failed: {str(e)}")
        raise

if __name__ == "__main__":
    main()