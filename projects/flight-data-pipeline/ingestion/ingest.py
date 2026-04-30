import json
import os
from datetime import datetime, timezone
from api_client import fetch_flights


def main():
    print("Fetching flight data from OpenSky...")

    data = fetch_flights()

    os.makedirs("data", exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    filename = f"data/raw_flights_{timestamp}.json"

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Saved data to {filename}")
    print(f"Number of flights: {len(data.get('states', []))}")


if __name__ == "__main__":
    main()