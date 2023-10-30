import pandas as pd
import numpy as np

class PalmaRatio:

    @staticmethod
    def measure(df):
        # Ensure the data is a numpy array for efficiency
        tokens = df['tokens'].to_numpy()

        # Sort the values in descending order for easy percentile computation
        tokens_sorted = np.sort(tokens)[::-1]

        # Determine the indices for the top 10% and bottom 40%
        top_10_idx = int(len(tokens) * 0.1)
        bottom_40_idx = int(len(tokens) * 0.4)

        # Sum the tokens for the top 10% and bottom 40%
        sum_top_10 = np.sum(tokens_sorted[:top_10_idx])
        sum_bottom_40 = np.sum(tokens_sorted[-bottom_40_idx:])

        # Calculate the Palma Ratio
        palma_ratio = sum_top_10 / sum_bottom_40 if sum_bottom_40 > 0 else np.nan

        return round(palma_ratio, 2)

def main():
    # Load the CSV file into a DataFrame
    file_path = 'data/25102023_sui.csv'  # Replace with the path to your CSV file
    df = pd.read_csv(file_path)

    # Call the measure method to calculate the Palma Ratio
    palma_ratio = PalmaRatio.measure(df)

    print(f'Palma Ratio: {palma_ratio}')

if __name__ == '__main__':
    main()
