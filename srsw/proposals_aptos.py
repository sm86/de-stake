import http.client
import json
import requests
import pandas as pd

class Aptos:
    MAINNET_VALIDATORS_DATA_URL = "https://storage.googleapis.com/aptos-mainnet/explorer/validator_stats_v2.json?cache-version=0"
    MAINNET_FULLNODE_DATA_URL = "fullnode.mainnet.aptoslabs.com"

    @classmethod
    def get_validators(cls):
        print('Retrieving data for Aptos')
        response = requests.get(cls.MAINNET_VALIDATORS_DATA_URL)

        if response.status_code != 200:
            print(f'Failed to retrieve data: {response.status_code}')
            return None
        
        validators_data = response.json()
        # In consistency with the explorer, seems to be showing fewer validators than the number here. 
        validator_info_list = [
            {
                'address': validator.get('owner_address', 'Unknown'),
                'proposals' : int(validator.get('last_epoch_performance', None).split('/')[1]),
                'tokens': cls.get_tokens(validator.get('owner_address', 'Unknown'))  # call getTokens on operator address
            }
            for validator in validators_data if validator.get('last_epoch_performance') is not None
        ]

        df = pd.DataFrame(validator_info_list)
        sorted_df = df.sort_values(by='tokens', ascending=False)
        print(sorted_df)
        csv_file = f'data/paper/02122023_aptos_proposals.csv'
        # Writing the DataFrame to a CSV file
        sorted_df.to_csv(csv_file, index=False)
        print(f'Data has been written to {csv_file}')
        return sorted_df

    @classmethod
    def get_tokens(cls, address):
        conn = http.client.HTTPSConnection(cls.MAINNET_FULLNODE_DATA_URL)
        headers = {'Accept': "application/json"}
        request_path = f"/v1/accounts/{address}/resource/0x1::stake::StakePool"
        try:
            conn.request("GET", request_path, headers=headers)
            res = conn.getresponse()
            data = res.read().decode("utf-8")
            json_object = json.loads(data)

            # It's a good practice to check if the keys exist before accessing them to avoid KeyError
            active_value = json_object.get('data', {}).get('active', {}).get('value')
            if active_value is not None:
                return int(active_value)
            else:
                raise KeyError("The required keys were not found in the JSON response")
        finally:
            conn.close()  # Ensure the connection is closed

if __name__ == '__main__':
    Aptos.get_validators()