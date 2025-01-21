import pandas as pd

import datetime
import pytz

# Get current date in IST
ist = pytz.timezone("Asia/Kolkata")
current_date = datetime.datetime.now(ist).date()
previous_date = current_date - datetime.timedelta(days=1)


# For ticket count dataset
def ticketcount_data_extraction(data):
    ticketcount_df = pd.DataFrame([data])
    ticketcount_df.insert(0, "Date", previous_date)
    return ticketcount_df


# For hourly data dataset
def hourly_data_extraction(data):
    payment_data = {}
    for payment_type in data["series"]:
        payment_data[payment_type["name"]] = payment_type["data"]

    # Create a DataFrame
    hourly_df = pd.DataFrame(payment_data)
    hourly_df.insert(0, "date_and_time", pd.to_datetime(data["categories"]))
    return hourly_df


# For station usage dataset
def station_data_extraction(data):
    def process_line_data(line_data):
        payment_data = {}
        for payment_type in line_data["series"]:
            payment_data[payment_type["name"]] = payment_type["data"]

        station_df = pd.DataFrame(payment_data)
        station_df.insert(0, "Station", line_data["categories"])

        # Add the date column
        station_df.insert(0, "Date", previous_date)
        station_df.insert(1, "Line", line_data["line"])
        return station_df

    all_line_dfs = {}

    for item in data:
        line_name = item["line"]
        df = process_line_data(item)
        all_line_dfs[line_name] = df
    return all_line_dfs
