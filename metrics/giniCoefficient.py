import pandas as pd
import numpy as np

class GiniCoefficient:

    @staticmethod
    def measure(df):
        # Ensure the data is a numpy array for efficiency
        tokens = df['tokens'].to_numpy()

        # Sort the values
        tokens_sorted = np.sort(tokens)

        # Get the cumulative sum of tokens and the cumulative count of validators
        cum_tokens = np.cumsum(tokens_sorted, dtype=float)
        total_tokens = cum_tokens[-1]

        # The Lorenz curve is the cumulative sum of tokens divided by the total number of tokens
        lorenz_curve = cum_tokens / total_tokens

        # Area under the Lorenz curve
        B = np.trapz(lorenz_curve, dx=1/len(tokens))

        # The Gini coefficient using the formula G = 1 - 2B
        gini_coefficient = 1 - 2 * B
        
        return round(gini_coefficient, 2)

def main():
    # Load the CSV file into a DataFrame
    file_path = 'data/25102023_sui.csv'  # Replace with the path to your CSV file
    df = pd.read_csv(file_path)
    
    # Call the measure method to calculate the Gini Coefficient
    gini_coefficient = GiniCoefficient.measure(df)
    
    print(f'Gini Coefficient: {gini_coefficient}')

if __name__ == '__main__':
    main()