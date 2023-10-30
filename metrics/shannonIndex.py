import pandas as pd
import numpy as np

class ShannonIndex:

    @staticmethod
    def measure(df):
        # Ensure the data is a numpy array for efficiency
        stakes = df['tokens'].to_numpy()
        
        # Calculate the total stake
        total_stake = np.sum(stakes)
        
        # Calculate the proportion of each stake
        proportions = stakes / total_stake
    
        # Filter out zero values to avoid log(0)
        nonzero_proportions = proportions[proportions > 0]
        
        # Compute the Shannon Index
        shannon_index = -np.sum(nonzero_proportions * np.log(nonzero_proportions))
        
        return round(shannon_index/np.log(len(nonzero_proportions)), 2)

def main():
    # Load the CSV file into a DataFrame
    file_path = 'data/25102023_sui.csv'  # Replace with the path to your CSV file
    df = pd.read_csv(file_path)
    
    # Call the measure method to calculate the Shannon Index
    shannon_index = ShannonIndex.measure(df)
    
    print(f'Shannon Index: {shannon_index}')

if __name__ == '__main__':
    main()