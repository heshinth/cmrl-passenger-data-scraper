import requests

from modules.data_extraction import (
    station_data_extraction,
    ticketcount_data_extraction,
    hourly_data_extraction,
)

from modules.data_store import ticket_count_dataset

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
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        ticketcount_df = ticketcount_data_extraction(data)
        ticket_count_dataset(ticketcount_df)

    else:
        print(f"Failed to fetch URL: {response.status_code}")


def scrape_hourly_data(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        hourly_data_extraction(data)


def scrape_station_data(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        formatted_data = station_data_extraction(data)
        print(formatted_data)

    else:
        print(f"Failed to fetch URL: {response.status_code}")


def main():
    scrape_ticketcount(allTicketCount_url)
    scrape_hourly_data(hourlybaseddata_url)
    scrape_station_data(stationData_url)


if __name__ == "__main__":
    main()
