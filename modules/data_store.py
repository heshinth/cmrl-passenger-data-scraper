import pandas as pd


def ticket_count_dataset(ticketcount_df: pd.DataFrame):
    file_path = "data/ticketcount.csv"
    try:
        current_data = pd.read_csv(file_path)
    except FileNotFoundError:
        current_data = pd.DataFrame(
            columns=ticketcount_df.columns
        )  # Initialize with columns

    combined_df = pd.concat([current_data, ticketcount_df], ignore_index=True)
    combined_df.to_csv(file_path, index=False)
    deduplication(file_path)


def hourly_dataset(ticketcount_df: pd.DataFrame):
    file_path = "data/hourly_data.csv"
    try:
        current_data = pd.read_csv(file_path)
    except FileNotFoundError:
        current_data = pd.DataFrame(
            columns=ticketcount_df.columns
        )  # Initialize with columns

    combined_df = pd.concat([current_data, ticketcount_df], ignore_index=True)
    combined_df.to_csv(file_path, index=False)
    deduplication(file_path)


def station_dataset(line, line_df):
    file_path = f"data/line_{line}_data.csv"
    try:
        current_data = pd.read_csv(file_path)
    except FileNotFoundError:
        current_data = pd.DataFrame(columns=line_df.columns)  # Initialize with columns

    combined_df = pd.concat([current_data, line_df], ignore_index=True)
    combined_df.to_csv(file_path, index=False)
    deduplication(file_path)


def deduplication(file_path):
    current_data = pd.read_csv(file_path)
    current_data.drop_duplicates(inplace=True)
    current_data.to_csv(file_path, index=False)
