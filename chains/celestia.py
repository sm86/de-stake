import requests
import pandas as pd
# import chains.save as save

class Celestia:
    URL = 'https://celestia.api.explorers.guru/api/v1/validators'
    
    @classmethod
    def get_validators(cls):
        print('Retrieving data for Celestia')
        response = requests.get(cls.URL)
        
        if response.status_code == 200:
            data = response.json()
            # Processing each validator's data
            validator_info_list = [
                {
                    'address': validator.get('moniker', None),
                    'tokens': int(validator.get('tokens', 0.0))
                }
                for validator in data
            ]
            # Creating a DataFrame
            df = pd.DataFrame(validator_info_list)
            # Sorting the DataFrame by votingPowerPercent
            sorted_df = df.sort_values(by='tokens', ascending=False)
            # save.write_csv(sorted_df, 'celestia')
            sorted_df.to_csv('data/04122023_celestia.csv', index=False)

            return sorted_df
        else:
            print(f'Failed to retrieve data: {response.status_code}')
            return None

if __name__ == '__main__':
    validator_dataframe = Celestia.get_validators()
    print(validator_dataframe)