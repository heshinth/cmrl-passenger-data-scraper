import pandas as pd

import datetime
import pytz


def station_data_extraction(data):
    def process_line_data(line_data):
        payment_data = {}
        for payment_type in line_data["series"]:
            payment_data[payment_type["name"]] = payment_type["data"]

        station_df = pd.DataFrame(payment_data, index=line_data["categories"])
        station_df.index.name = "Station"

        # Get current date in IST
        ist = pytz.timezone("Asia/Kolkata")
        current_date = datetime.datetime.now(ist).date()

        # Add the date column
        station_df.insert(0, "Date", current_date)
        station_df.insert(1, "Line", line_data["line"])
        return station_df

    all_line_dfs = {}

    for item in data:
        line_name = item["line"]
        df = process_line_data(item)
        all_line_dfs[line_name] = df
    return all_line_dfs
