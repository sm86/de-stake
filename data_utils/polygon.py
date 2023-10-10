import requests
import pandas as pd
from datetime import datetime

class Polygon:
    URL = 'https://validator.info/api/polygon/validators?timeframe=week&nameContains=&activeValidators=true'

    @classmethod
    def get_validators(cls):
        print('Retrieving data for Polygon')
        response = requests.get(cls.URL)

        if response.status_code != 200:
            print(f'Failed to retrieve data: {response.status_code}')
            return None
        
        response_data = response.json()
        validators_list = response_data.get('list', [])
        validator_info_list = [
            {
                'validator_id': validator.get('name', ''),
                'tokens': int(validator.get('totalStaked', 0))
            }
            for index, validator in enumerate(validators_list, start=1)
        ]

        df = pd.DataFrame(validator_info_list)
        sorted_df = df.sort_values(by='tokens', ascending=False)
        write_csv(sorted_df)
        return sorted_df

def write_csv(df):
    # Getting the current date
    current_date = datetime.now().strftime('%d-%m-%Y')
    # Including the date in the filename
    csv_file = f'data/polygon_{current_date}.csv'
    # Writing the DataFrame to a CSV file
    df.to_csv(csv_file, index=False)
    print(f'Data has been written to {csv_file}')

if __name__ == '__main__':
    Polygon.get_validators()
