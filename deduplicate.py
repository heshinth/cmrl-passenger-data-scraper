import pandas as pd

file_path = "data/ticketcount.csv"
current_data = pd.read_csv(file_path)
current_data.drop_duplicates(inplace=True)

current_data.to_csv(file_path, index=False)
