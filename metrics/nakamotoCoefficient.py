import pandas as pd

class NakamotoCoefficient:
    
    @staticmethod
    def measureLivenessNC(df):
        # Ensure the DataFrame is sorted in descending order of tokens (voting power)
        df = df.sort_values(by='tokens', ascending=False)
        
        # Calculate the threshold (33% of total voting power)
        total_voting_power = df['tokens'].sum()
        threshold_voting_power = total_voting_power * 0.33
        
        # Initialize variables
        accumulated_voting_power = 0
        validator_count = 0
        
        # Loop through the DataFrame to find the minimum number of validators 
        # that add up to at least 33% of total voting power
        for _, row in df.iterrows():
            accumulated_voting_power += row['tokens']
            validator_count += 1
            if accumulated_voting_power >= threshold_voting_power:
                break
        
        # Calculate the percentage of total validators
        total_validators = len(df)
        percentage = (validator_count / total_validators) * 100
        
        return validator_count, round(percentage,2)
    
    @staticmethod
    def measureSafetyNC(df):
        # Ensure the DataFrame is sorted in descending order of tokens (voting power)
        df = df.sort_values(by='tokens', ascending=False)
        
        # Calculate the threshold (66% of total voting power)
        total_voting_power = df['tokens'].sum()
        threshold_voting_power = total_voting_power * 0.66
        
        # Initialize variables
        accumulated_voting_power = 0
        validator_count = 0
        
        # Loop through the DataFrame to find the minimum number of validators 
        # that add up to at least 33% of total voting power
        for _, row in df.iterrows():
            accumulated_voting_power += row['tokens']
            validator_count += 1
            if accumulated_voting_power >= threshold_voting_power:
                break
        
        # Calculate the percentage of total validators
        total_validators = len(df)
        percentage = (validator_count / total_validators) * 100
        
        return validator_count, round(percentage,2)


def main():
    # Load the CSV file into a DataFrame
    file_path = 'data/22112023_celo.csv'  # Replace with the path to your CSV file
    df = pd.read_csv(file_path)
  
    # Call the measure method to calculate the Nakamoto Coefficient
    nakamoto_coefficient, percentage = NakamotoCoefficient.measureSafetyNC(df)
    
    print(f'Nakamoto Coefficient: {nakamoto_coefficient}')
    print(f'Percentage of Total Validators: {percentage:.2f}%')

    # Call the measure method to calculate the Nakamoto Coefficient
    nakamoto_coefficient, percentage = NakamotoCoefficient.measureLivenessNC(df)
    
    print(f'Nakamoto Coefficient: {nakamoto_coefficient}')
    print(f'Percentage of Total Validators: {percentage:.2f}%')


if __name__ == '__main__':
    main()
