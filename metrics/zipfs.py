import pandas as pd
import numpy as np
from scipy.stats import linregress

class ZipfCoefficient:
    
    @staticmethod
    def calculate_zipf(df, col='tokens'):
        # Sort weights in descending order and filter out zeros
        weights = np.sort(df[col].to_numpy())[::-1]
        weights = weights[weights > 0]  # Filter out zero values to avoid log(0)
        
        # Rank each validator (1-based rank)
        ranks = np.arange(1, len(weights) + 1)

        # Perform log-log transformation
        log_ranks = np.log(ranks)
        log_weights = np.log(weights)

        # Calculate the slope (Z) of the log-log regression
        slope, _, _, _, _ = linregress(log_ranks, log_weights)
        
        # Zipf's Law coefficient is the negative of the slope
        zipf_coefficient = -slope
        return round(zipf_coefficient, 3)

def main():
    # Load the CSV file into a DataFrame
    file_path = 'data/25102023_axelar.csv'  # Replace with the path to your CSV file
    df = pd.read_csv(file_path)
    
    # Calculate Zipf's Law Coefficient
    zipf_coefficient = ZipfCoefficient.calculate_zipf(df)
    print(f"Zipf's Law Coefficient (Z): {zipf_coefficient}")

if __name__ == '__main__':
    main()
