import json
import os
from datetime import datetime, timezone
from api_client import fetch_flights
from config import OUTPUT_DIR
from logger import logger


def main():
    logger.info("Starting ingestion job")

    try:
        data = fetch_flights()

        now = datetime.now(timezone.utc)
        timestamp = now.strftime("%Y%m%d_%H%M%S")

        partition_path = os.path.join(
            OUTPUT_DIR,
            f"yeah={now.year}",
            f"month={now.month:02}",
            f"day={now.day:02}"
        )

        os.makedirs(partition_path, exist_ok=True)

        filename = f"flights_{timestamp}.json"

        output_path = os.path.join(
            partition_path,
            filename
        )

        # Add ingestion metadata
        wrapped_data = {
            "ingestion_time": timestamp,
            "source": "opensky",
            "data": data
        }

        with open(output_path, "w") as f:
            json.dump(wrapped_data, f)

        record_count = len(data.get("states", []))

        logger.info(f"Ingestion successful: {record_count} records saved to {output_path}")
        print(f"Saved {record_count} records")

    except Exception as e:
        logger.error(f"Ingestion failed: {str(e)}")
        raise

if __name__ == "__main__":
    main()