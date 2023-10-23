import requests
import pandas as pd

import utils

class Osmosis:
    URL = 'https://lcd-osmosis.keplr.app/staking/validators'

    @classmethod
    def get_validators(cls):
        print('Retrieving data for Osmosis')
        response = requests.get(cls.URL)

        if response.status_code == 200:
            data = response.json()
            validators = data.get('result', [])

            # Collecting specified values for each validator
            validator_info_list = [
                {
                    # 'address': validator.get('operator_address', 'Unknown'),
                    'tokens': int(validator.get('tokens', '0'))  # Assuming 0 if tokens is not found,
                    'address': validator.get('description', {}).get('moniker', 'Unknown')
                }
                for validator in validators
            ]

            # Creating a DataFrame
            df = pd.DataFrame(validator_info_list)

            # Sorting the DataFrame based on tokens (assumed to be numeric)
            sorted_df = df.sort_values(by='tokens', ascending=False)
            utils.write_csv(sorted_df, 'osmosis')
            return sorted_df
        else:
            print(f'Failed to retrieve data: {response.status_code}')
            return None

if __name__ == '__main__':
    validator_dataframe = Osmosis.get_validators()
