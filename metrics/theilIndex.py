import pandas as pd
import numpy as np

class TheilIndex:

    @staticmethod
    def measure(df):
        # Ensure the data is a numpy array for efficiency
        tokens = df['tokens'].to_numpy()
        
        # Calculate the mean tokens
        mean_tokens = np.mean(tokens)
        
        # Avoid division by zero and log(0) issues by replacing 0 with a very small value
        tokens[tokens == 0] = 1e-10
        mean_tokens = max(mean_tokens, 1e-10)
        
        # Compute the Theil Index
        theil_index = np.mean((tokens / mean_tokens) * np.log(tokens / mean_tokens))
        
        return round(theil_index, 2)

def main():
    # Load the CSV file into a DataFrame
    file_path = 'data/25102023_sui.csv'  # Replace with the path to your CSV file
    df = pd.read_csv(file_path)
    
    # Call the measure method to calculate the Theil Index
    theil_index = TheilIndex.measure(df)
    
    print(f'Theil Index: {theil_index}')

if __name__ == '__main__':
    main()
