import requests
import json
import pandas as pd

import chains.save as save


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
                    'address': validator.get('operator_address', 'Unknown'),
                    'tokens': int(validator.get('tokens', '0'))  # Assuming 0 if tokens is not found
                }
                for validator in validators
            ]
            # Creating a DataFrame
            df = pd.DataFrame(validator_info_list)
            # Sorting the DataFrame based on tokens (assumed to be numeric)
            sorted_df = df.sort_values(by='tokens', ascending=False)
            save.write_csv(sorted_df, 'cosmos')
            return sorted_df
        else:
            print(f'Failed to retrieve data: {response.status_code}')
            return None

if __name__ == '__main__':
    validator_dataframe = Cosmos.get_validators()
