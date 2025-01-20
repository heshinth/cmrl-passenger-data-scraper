import pandas as pd


# For Ticket count dataset
def ticket_count_dataset(ticketcount_df):
    file_path = "data/ticketcount.csv"

    try:
        # Try reading the existing CSV file
        existing_data = pd.read_csv(file_path)

        # Check if the file is empty (no rows)
        if existing_data.empty:
            combined_data = ticketcount_df  # If empty, just use the new DataFrame
        else:
            # Combine new data with existing data and drop duplicates
            combined_data = pd.concat([existing_data, ticketcount_df]).drop_duplicates()

        # Save back to the file
        combined_data.to_csv(file_path, index=False)

    except pd.errors.EmptyDataError:
        # If the file is empty or doesn't contain valid data, write new data
        ticketcount_df.to_csv(file_path, index=False)

    except FileNotFoundError:
        # If the file doesn't exist, write new data
        ticketcount_df.to_csv(file_path, index=False)
