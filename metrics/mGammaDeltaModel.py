import pandas as pd
import numpy as np

class mGammaDeltaModel:

    @staticmethod
    def getDelta(df, gamma):
        # Sort the DataFrame by 'tokens' in descending order
        sorted_df = df.sort_values(by='tokens', ascending=True).reset_index(drop=True)
        sorted_df = sorted_df[sorted_df['tokens'] != 0]

        # Calculate the index for the gamma percentile
        gamma_index = max(int(np.ceil(gamma / 100 * len(sorted_df)) - 1), 0)

        # Get the tokens for the richest and gamma percentile
        richest_tokens = sorted_df.iloc[len(sorted_df)-1]['tokens']
        gamma_percentile_tokens = sorted_df.iloc[gamma_index]['tokens']
        
        # Check to prevent division by zero
        if gamma_percentile_tokens == 0:
            return float('inf')  # or another appropriate value

        # Calculate delta
        delta = richest_tokens / gamma_percentile_tokens - 1
        return round(delta, 2)

    @staticmethod
    def getDeltaStepFunction(df):
        delta_values = []
        for gamma in range(0, 101, 5):
            delta = mGammaDeltaModel.getDelta(df, gamma)
            delta_values.append(delta)
        return delta_values


def main():
    # Load the CSV file into a DataFrame
    file_path = 'data/25102023_sui.csv'  # Replace with the path to your CSV file
    df = pd.read_csv(file_path)
    
    # Get delta values at intervals of 10 from 0 to 100
    delta_step_function = mGammaDeltaModel.getDeltaStepFunction(df)
    
    print(delta_step_function)

if __name__ == '__main__':
    main()