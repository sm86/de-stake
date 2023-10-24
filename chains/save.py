from datetime import datetime
import pandas as pd

def write_csv(df, network):
    # Getting the current date
    current_date = datetime.now().strftime('%d%m%Y')
    # Including the date in the filename
    csv_file = f'data/{current_date}_{network}.csv'
    # Writing the DataFrame to a CSV file
    df.to_csv(csv_file, index=False)
    print(f'Data has been written to {csv_file}')
