import pandas as pd
import numpy as np

class HHICoefficient:

    @staticmethod
    def measure(df,col='tokens'):
        # Convert tokens column to a numpy array
        weights = df[col].to_numpy()

        # Calculate the total tokens to derive market shares
        total_weight = weights.sum()

        # Calculate market shares as the proportion of each validator's tokens
        market_shares = weights / total_weight

        # HHI calculation as the sum of the squares of market shares
        hhi_index = np.sum(market_shares ** 2) 
        
        return round(hhi_index, 3)

def main():
    # Load the CSV file into a DataFrame
    file_path = 'data/25102023_sui.csv'  # Replace with the path to your CSV file
    df = pd.read_csv(file_path)
    
    # Call the measure method to calculate the HHI
    hhi_index = HHICoefficient.measure(df)
    
    print(f'Herfindahl-Hirschman Index (HHI): {hhi_index}')

if __name__ == '__main__':
    main()
