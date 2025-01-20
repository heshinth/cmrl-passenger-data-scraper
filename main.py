import requests
import json
import pprint


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
    data = response.content
    data = data.decode("utf-8")
    json_str = json.loads(data)
    pprint.pp(json_str)


def main():
    scrape_ticketcount(allTicketCount_url)


if __name__ == "__main__":
    main()
