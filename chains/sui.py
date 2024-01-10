import requests
import pandas as pd

import chains.utils as utils

class Sui:
    URL = 'https://fullnode.mainnet.sui.io'

    @classmethod
    def get_validators(cls):
        print('Retrieving data for Sui')
        headers = {
            'Content-Type': 'application/json',
        }
        data = {
            'jsonrpc': '2.0',
            'id': 1,
            'method': 'suix_getLatestSuiSystemState',
            'params': [],
        }
        response = requests.post(cls.URL, headers=headers, json=data)

        if response.status_code != 200:
            print(f'Failed to retrieve data: {response.status_code}')
            return None

        response_data = response.json()
        active_validators = response_data.get('result', {}).get('activeValidators', [])
        validator_info_list = [
            {
                'address': validator.get('name', ''),
                'tokens': int(validator.get('stakingPoolSuiBalance', '0')),
                'domain' : validator.get('netAddress', '').split('/')[2]
            }
            for index, validator in enumerate(active_validators, start=1)
        ]
        df = pd.DataFrame(validator_info_list)
        
        # Use domain to find the current IP and drop the domain 
        df['ip_address'] = df['domain'].apply(utils.get_ip_address)
        df.drop('domain', axis=1, inplace=True)
        
        sorted_df = df.sort_values(by='tokens', ascending=False)
        utils.write_csv(sorted_df, 'sui')
        return sorted_df

if __name__ == '__main__':
    validator_dataframe = Sui.get_validators()