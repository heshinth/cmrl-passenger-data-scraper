import requests
import pprint
import pandas as pd

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
        # pprint.pp(data)
        ticketcount_df = pd.DataFrame([data])
        print(ticketcount_df)

    else:
        print(f"Failed to fetch URL: {response.status_code}")


def scrape_hourly_data(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # pprint.pp(data)
        # Extract data for each series
        series_data = {}
        for series in data["series"]:
            series_data[series["name"]] = series["data"]

        # Create a DataFrame
        df = pd.DataFrame(series_data, index=pd.to_datetime(data["categories"]))
        df.index.name = "timestamp"
        print(df.info())
    else:
        print(f"Failed to fetch URL: {response.status_code}")


def scrape_station_data(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        pprint.pp(data)
        ticketcount_df = pd.DataFrame([data])
        print(ticketcount_df)

    else:
        print(f"Failed to fetch URL: {response.status_code}")


def main():
    # scrape_ticketcount(allTicketCount_url)
    scrape_hourly_data(hourlybaseddata_url)
    # scrape_station_data(stationData_url)


if __name__ == "__main__":
    main()
