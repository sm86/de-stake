import requests
import pandas as pd

import chains.save as save

class Axelar:
    BASE_URL = 'https://rpc-axelar.imperator.co/dump_consensus_state'

    @classmethod
    def get_validators(cls):
        print('Retrieving data for Axelar')

        response = requests.get(cls.BASE_URL)
        
        if response.status_code != 200:
            print(f'Failed to retrieve Axelar data: {response.status_code}')
            return None

        data = response.json()
        validators_data = data.get('result', {}).get('round_state', {}).get('validators', {}).get('validators', [])

        validator_info_list = []
        for validator in validators_data:
            validator_info = {
                'address': validator.get('address', 'Unknown'),
                'tokens': int(validator.get('voting_power', 'Unknown'))
            }
            validator_info_list.append(validator_info)
        
        # Creating a DataFrame
        df = pd.DataFrame(validator_info_list)
        # Sorting the DataFrame based on tokens (assuming tokens are numeric)
        sorted_df = df.sort_values(by='tokens', ascending=False)
        save.write_csv(sorted_df, 'axelar')
        return sorted_df

if __name__ == '__main__':
    Axelar.get_validators()
