import requests
import pandas as pd
from datetime import datetime

class Binance:
    BASE_URL = 'https://api.binance.org/v1/staking/chains/bsc/validators'

    @classmethod
    def get_validators(cls):
        print('Retrieving data for Binance')

        page_limit, page_offset = 50, 0
        validator_info_list = []

        while True:
            url = f'{cls.BASE_URL}?limit={page_limit}&offset={page_offset}'
            response = requests.get(url)
            
            if response.status_code != 200:
                print(f'Failed to retrieve data: {response.status_code}')
                return None

            data = response.json()
            validators = data.get('validators', [])

            # Break if no more entries left
            if len(validators) == 0:
                break

            for validator in validators:
                validator_info = {
                    'validator_id': validator.get('validator', 'Unknown'),
                    'tokens': validator.get('votingPower', 'Unknown')
                }
                validator_info_list.append(validator_info)

            # Increment counters
            page_offset += page_limit
        
        # Creating a DataFrame
        df = pd.DataFrame(validator_info_list)
        # Sorting the DataFrame based on tokens (assuming tokens are numeric)
        sorted_df = df.sort_values(by='tokens', ascending=False)
        return sorted_df
def write_csv(df):
    current_date = datetime.now().strftime('%Y-%m-%d')
    # Including the date in the filename
    csv_file = f'data/binance_{current_date}.csv'
    # Writing the DataFrame to a CSV file
    df.to_csv(csv_file, index=False)
    print(f'Data has been written to {csv_file}')

if __name__ == '__main__':
    Binance.get_validators()