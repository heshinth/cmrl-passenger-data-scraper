import asyncio
import json
import os
import sys
import httpx
from modules.data_extraction import (
    station_data_extraction,
    ticketcount_data_extraction,
    hourly_data_extraction,
)
from modules.data_store import ticket_count_dataset, hourly_dataset, station_dataset
from modules.logger import setup_logger

# Setup logger
logger = setup_logger()

# Configurable API base URL
API_BASE_URL = os.getenv(
    "CMRL_API_BASE",
    "https://commuters-dataapi.chennaimetrorail.org/api/PassengerFlow",
)

allTicketCount_url = f"{API_BASE_URL}/allTicketCount/1"
hourlybaseddata_url = f"{API_BASE_URL}/hourlybaseddata/1"
stationData_url = f"{API_BASE_URL}/stationData/1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}


def save_debug_payload(name, payload):
    """Saves unexpected or broken API responses for troubleshooting."""
    try:
        os.makedirs("logs", exist_ok=True)
        file_path = f"logs/debug_{name}.json"
        with open(file_path, "w", encoding="utf-8") as f:
            if isinstance(payload, (dict, list)):
                json.dump(payload, f, indent=2)
            else:
                f.write(str(payload))
        logger.info(f"Saved diagnostic payload to {file_path}")
    except Exception as e:
        logger.error(f"Failed to save debug payload: {e}")


async def scrape_ticketcount(client, url):
    logger.info("Starting ticket count data scraping")
    try:
        response = await client.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            try:
                ticketcount_df = ticketcount_data_extraction(data)
                ticket_count_dataset(ticketcount_df)
                logger.info("Successfully scraped and stored ticket count data")
                return True
            except Exception as e:
                logger.error(f"Failed to extract ticket count: {e}", exc_info=True)
                save_debug_payload("ticketcount", data)
                return False
        else:
            logger.error(f"Failed to fetch ticket count data: HTTP {response.status_code}")
            save_debug_payload("ticketcount", response.text)
            return False
    except Exception as e:
        logger.error(f"Error fetching ticket count: {e}", exc_info=True)
        return False


async def scrape_hourly_data(client, url):
    logger.info("Starting hourly data scraping")
    try:
        response = await client.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            try:
                hourly_df = hourly_data_extraction(data)
                hourly_dataset(hourly_df)
                logger.info("Successfully scraped and stored hourly data")
                return True
            except Exception as e:
                logger.error(f"Failed to extract hourly data: {e}", exc_info=True)
                save_debug_payload("hourly", data)
                return False
        else:
            logger.error(f"Failed to fetch hourly data: HTTP {response.status_code}")
            save_debug_payload("hourly", response.text)
            return False
    except Exception as e:
        logger.error(f"Error fetching hourly data: {e}", exc_info=True)
        return False


async def scrape_station_data(client, url):
    logger.info("Starting station data scraping")
    try:
        response = await client.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            try:
                formatted_data = station_data_extraction(data)
                for line_no, line_df in formatted_data.items():
                    station_dataset(line_no, line_df)
                    logger.info(f"Successfully stored data for line {line_no}")
                logger.info("Successfully scraped and stored all station data")
                return True
            except Exception as e:
                logger.error(f"Failed to extract station data: {e}", exc_info=True)
                save_debug_payload("stationData", data)
                return False
        else:
            logger.error(f"Failed to fetch station data: HTTP {response.status_code}")
            save_debug_payload("stationData", response.text)
            return False
    except Exception as e:
        logger.error(f"Error fetching station data: {e}", exc_info=True)
        return False


async def main():
    logger.info("Starting CMRL data scraping process")
    async with httpx.AsyncClient(timeout=60.0) as client:
        results = await asyncio.gather(
            scrape_ticketcount(client, allTicketCount_url),
            scrape_hourly_data(client, hourlybaseddata_url),
            scrape_station_data(client, stationData_url),
            return_exceptions=True,
        )

        success = all(res is True for res in results)
        if success:
            logger.info("Completed CMRL data scraping process successfully")
            return 0
        else:
            logger.error("CMRL data scraping finished with errors")
            return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
