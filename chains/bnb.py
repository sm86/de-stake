import requests
import pandas as pd

import chains.utils as utils

class Bnb:
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
                print(f'Failed to retrieve Binance data: {response.status_code}')
                return None

            data = response.json()
            validators = data.get('validators', [])

            # Break if no more entries left
            if len(validators) == 0:
                break

            for validator in validators:
                print(validator)
                validator_info = {
                    'address': validator.get('validator', 'Unknown'),
                    # 'tokens': int(validator.get('votingPower', 'Unknown'))
                }
                validator_info_list.append(validator_info)

            # Increment counters
            page_offset += page_limit
        
        # Creating a DataFrame
        df = pd.DataFrame(validator_info_list)
        # Sorting the DataFrame based on tokens (assuming tokens are numeric)
        # sorted_df = df.sort_values(by='tokens', ascending=False)
        # utils.write_csv(sorted_df, 'binance')
        # return sorted_df

if __name__ == '__main__':
    Binance.get_validators()