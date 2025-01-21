import requests
from modules.data_extraction import (
    station_data_extraction,
    ticketcount_data_extraction,
    hourly_data_extraction,
)
from modules.data_store import ticket_count_dataset, hourly_dataset, station_dataset
from modules.logger import setup_logger

# Setup logger
logger = setup_logger()

allTicketCount_url = (
    "https://commuters-dataapi.chennaimetrorail.org/api/PassengerFlow/allTicketCount/1"
)
hourlybaseddata_url = (
    "https://commuters-dataapi.chennaimetrorail.org/api/PassengerFlow/hourlybaseddata/1"
)
stationData_url = (
    "https://commuters-dataapi.chennaimetrorail.org/api/PassengerFlow/stationData/1"
)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}


def scrape_ticketcount(url):
    logger.info("Starting ticket count data scraping")
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        ticketcount_df = ticketcount_data_extraction(data)
        ticket_count_dataset(ticketcount_df)
        logger.info("Successfully scraped and stored ticket count data")
    else:
        logger.error(f"Failed to fetch ticket count data: {response.status_code}")


def scrape_hourly_data(url):
    logger.info("Starting hourly data scraping")
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        hourly_df = hourly_data_extraction(data)
        hourly_dataset(hourly_df)
        logger.info("Successfully scraped and stored hourly data")
    else:
        logger.error(f"Failed to fetch hourly data: {response.status_code}")


def scrape_station_data(url):
    logger.info("Starting station data scraping")
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        formatted_data = station_data_extraction(data)
        for line_no, line_df in formatted_data.items():
            station_dataset(line_no, line_df)
            logger.info(f"Successfully stored data for line {line_no}")
        logger.info("Successfully scraped and stored all station data")
    else:
        logger.error(f"Failed to fetch station data: {response.status_code}")


def main():
    logger.info("Starting CMRL data scraping process")
    try:
        scrape_ticketcount(allTicketCount_url)
        scrape_hourly_data(hourlybaseddata_url)
        scrape_station_data(stationData_url)
        logger.info("Completed CMRL data scraping process")
    except Exception as e:
        logger.error(f"An error occurred during scraping: {str(e)}", exc_info=True)


if __name__ == "__main__":
    main()
