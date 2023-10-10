import requests
import json
import pandas as pd

from datetime import datetime


class Cosmos:
    URL = 'https://proxy.atomscan.com/cosmoshub-lcd/cosmos/staking/v1beta1/validators?page.offset=1&pagination.limit=500&status=BOND_STATUS_BONDED'
    
    @classmethod
    def get_validators(cls):
        print('Retrieving data for Cosmos')
        response = requests.get(cls.URL)
        
        if response.status_code == 200:
            data = response.json()
            validators = data.get('validators', [])
            # Collecting specified values for each validator
            validator_info_list = [
                {
                    'operator_address': validator.get('operator_address', 'Unknown'),
                    'tokens': int(validator.get('tokens', '0'))  # Assuming 0 if tokens is not found
                }
                for validator in validators
            ]
            # Creating a DataFrame
            df = pd.DataFrame(validator_info_list)
            # Sorting the DataFrame based on tokens (assumed to be numeric)
            sorted_df = df.sort_values(by='tokens', ascending=False)
            write_csv(sorted_df)
            return sorted_df
        else:
            print(f'Failed to retrieve data: {response.status_code}')
            return None
def write_csv(df):
    # Getting the current date
    current_date = datetime.now().strftime('%d-%m-%Y')
    # Including the date in the filename
    csv_file = f'data/raw_data/cosmos_{current_date}.csv'
    # Writing the DataFrame to a CSV file
    df.to_csv(csv_file, index=False)
    print(f'Data has been written to {csv_file}')

if __name__ == '__main__':
    validator_dataframe = Cosmos.get_validators()
