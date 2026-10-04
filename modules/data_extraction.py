import pandas as pd
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# Get current date in IST
ist = ZoneInfo("Asia/Kolkata")
current_date = datetime.now(ist).date()
previous_date = str(current_date - timedelta(days=1))


# For ticket count dataset
def ticketcount_data_extraction(data):
    if not isinstance(data, dict) or "totalTickets" not in data:
        raise ValueError(
            f"Unexpected ticket count schema: expected dictionary with 'totalTickets', got {list(data.keys()) if isinstance(data, dict) else type(data)}"
        )
    ticketcount_df = pd.DataFrame([data])
    ticketcount_df.insert(0, "Date", previous_date)
    return ticketcount_df


# For hourly data dataset
def hourly_data_extraction(data):
    if not isinstance(data, dict) or "series" not in data or "categories" not in data:
        raise ValueError(
            f"Unexpected hourly data schema: expected 'series' and 'categories', got {list(data.keys()) if isinstance(data, dict) else type(data)}"
        )
    payment_data = {}
    for payment_type in data["series"]:
        payment_data[payment_type["name"]] = payment_type["data"]

    # Create a DataFrame
    hourly_df = pd.DataFrame(payment_data)
    hourly_df.insert(0, "date_and_time", pd.to_datetime(data["categories"]))
    return hourly_df


# For station usage dataset
def station_data_extraction(data):
    if not isinstance(data, list) or (data and ("line" not in data[0] or "series" not in data[0] or "categories" not in data[0])):
        raise ValueError(
            f"Unexpected station data schema: expected list of line objects with 'line', 'categories', 'series'. Got {data[:1] if isinstance(data, list) else type(data)}"
        )

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
