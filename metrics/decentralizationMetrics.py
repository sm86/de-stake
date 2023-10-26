import pandas as pd
import os
import glob

from nakamotoCoefficient import NakamotoCoefficient
from giniCoefficient import GiniCoefficient


class DecentralizationMetrics:

    @staticmethod
    def calculate_metrics(date):
        # Define the path to the data folder and the pattern for the date
        data_folder_path = 'data'
        file_pattern = f"{date}_*"

        # Get the list of files for the given date
        files = glob.glob(os.path.join(data_folder_path, file_pattern))

        # Initialize an empty DataFrame to store the results
        results_df = pd.DataFrame(columns=['blockchain', 'N', 'nc_safety', 'nc_safety_percent', 'nc_liveness', 'nc_liveness_percent', 'gini'])

        # Loop through each file, calculate the metrics, and append the results to the results_df
        for file in files:
            # Extract the blockchain name from the file name
            blockchain_name = os.path.basename(file).split('_')[1].split('.')[0]

            # Load the CSV file into a DataFrame
            df = pd.read_csv(file)
            
            # Calculate the Nakamoto and Gini Coefficients
            ncSafety, safetyNCPercent = NakamotoCoefficient.measureSafetyNC(df)
            ncLiveness, livenessNCPercent = NakamotoCoefficient.measureLivenessNC(df)
            gini = GiniCoefficient.measure(df)
            
            results_df = pd.concat([pd.DataFrame([[blockchain_name, len(df), ncSafety, safetyNCPercent, ncLiveness, livenessNCPercent, gini]], columns=results_df.columns), results_df], ignore_index=True)

        return results_df

def main():
    # Assume the date is provided as a string in the format 'ddmmyyyy'
    date = '26102023'
    
    # Call the calculate_metrics method to calculate the decentralization metrics
    results_df = DecentralizationMetrics.calculate_metrics(date)
    
    # Print the results
    print(results_df)

if __name__ == '__main__':
    main()