import pandas as pd


def ticket_count_dataset(ticketcount_df: pd.DataFrame):
    file_path = "data/passenger_ticket_count.csv"
    try:
        current_data = pd.read_csv(file_path)
    except FileNotFoundError:
        current_data = pd.DataFrame(
            columns=ticketcount_df.columns
        )  # Initialize with columns

    combined_df = pd.concat([current_data, ticketcount_df], ignore_index=True)
    combined_df.drop_duplicates(subset=["Date"], keep="last", inplace=True)
    combined_df.to_csv(file_path, index=False)


def hourly_dataset(hourly_df: pd.DataFrame):
    file_path = "data/passenger_flow_hourly.csv"
    try:
        current_data = pd.read_csv(file_path)
    except FileNotFoundError:
        current_data = pd.DataFrame(
            columns=hourly_df.columns
        )  # Initialize with columns

    combined_df = pd.concat([current_data, hourly_df], ignore_index=True)
    combined_df["date_and_time"] = combined_df["date_and_time"].astype(str)
    combined_df.drop_duplicates(subset=["date_and_time"], keep="last", inplace=True)
    combined_df.to_csv(file_path, index=False)


def station_dataset(line, line_df):
    line_clean = f"{int(line):02d}" if str(line).isdigit() else str(line)
    file_path = f"data/passenger_flow_line_{line_clean}.csv"
    try:
        current_data = pd.read_csv(file_path)
    except FileNotFoundError:
        current_data = pd.DataFrame(
            columns=line_df.columns
        )  # Initialize with columns

    combined_df = pd.concat([current_data, line_df], ignore_index=True)
    combined_df.drop_duplicates(subset=["Date", "Station"], keep="last", inplace=True)
    combined_df.to_csv(file_path, index=False)


def deduplication(file_path):
    current_data = pd.read_csv(file_path)
    current_data.drop_duplicates(inplace=True)
    current_data.to_csv(file_path, index=False)
