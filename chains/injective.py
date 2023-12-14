import requests
import pandas as pd
import chains.save as save

class Injective:
    URL = 'https://lcd.injective.network/cosmos/base/tendermint/v1beta1/validatorsets/latest'
    
    @classmethod
    def get_validators(cls):
        print('Retrieving data for Injective Protocol')
        response = requests.get(cls.URL)
        
        if response.status_code == 200:
            data = response.json()
            validators = data.get('validators', [])

            # Processing each validator's data
            validator_info_list = [
                {
                    'address': validator.get('address', None),
                    'tokens': int(validator.get('voting_power', 0))
                }
                for validator in validators
            ]

            # Creating a DataFrame
            df = pd.DataFrame(validator_info_list)

            # Sorting the DataFrame by voting_power
            sorted_df = df.sort_values(by='tokens', ascending=False)

            # Saving the data to a CSV file
            save.write_csv(sorted_df, 'injective')
            return sorted_df
        else:
            print(f'Failed to retrieve data: {response.status_code}')
            return None

if __name__ == '__main__':
    validator_dataframe = Injective.get_validators()
    print(validator_dataframe)
