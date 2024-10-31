import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

from nakamotoCoefficient import NakamotoCoefficient
from giniCoefficient import GiniCoefficient
from HHIcoefficient import HHICoefficient
from shapleyValue import ShapleyGini
from zipfs import ZipfCoefficient

class DecentralizationMetrics:

    # Three scales:
    # sw - Stake weight linear
    # srsw - Square root stake weight 
    # lsw - Logarithmic stake weight
    @staticmethod
    def calculate_metrics(scale='sw'):
        # Define the path to the data folder
        folder_path = 'data/tnsm/'
        
        # Get the list of files for the given date
        files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

        # Initialize an empty DataFrame to store the results
        results_df = pd.DataFrame(columns=['blockchain', 'scale', 'N', 'nc_safety',  'nc_liveness', 'gini', 'hhi', 'shapley_liveness', 'shapley_safety', 'shapley_correlation', 'zipfs'])

        scales = ['tokens']

        # Loop through each file, calculate the metrics, and append the results to the results_df
        for file in files:
            # Extract the blockchain name from the file name
            blockchain_name = os.path.basename(file).split('_')[1].split('.')[0]
            # Load the CSV file into a DataFrame
            df = pd.read_csv(folder_path+file)
            print(blockchain_name) 
            df['srsw'] = np.sqrt(df['tokens'])
            df['lsw'] = np.log(df['tokens']+1)           
            
            for scale in scales:                 
                col = scale     
                _, safetyNCPercent = NakamotoCoefficient.measureSafetyNC(df,col)
                _, livenessNCPercent = NakamotoCoefficient.measureLivenessNC(df,col)
                gini = GiniCoefficient.measure(df,col)
                hhi = HHICoefficient.measure(df,col)
                shapley_liveness, shapley_safety, shapley_correlation = ShapleyGini.measure(df,col)
                zipf = ZipfCoefficient.calculate_zipf(df,col)
                
                results_df = pd.concat([pd.DataFrame([[blockchain_name, scale, len(df),  safetyNCPercent, livenessNCPercent, gini, hhi, shapley_liveness, shapley_safety, shapley_correlation, zipf]], columns=results_df.columns), results_df], ignore_index=True)
            
        results_df = results_df.sort_values(by='blockchain', ascending=True, ignore_index=True)
        return results_df

def getMetrics():
    # Call the calculate_metrics method to calculate the decentralization metrics
    results_df = DecentralizationMetrics.calculate_metrics()
    # Define the path to save the result CSV
    output_path = 'tnsm/results/empiricial-analysis-tokens-correlation.csv'
    
    # Ensure the folder exists before saving
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save the results DataFrame to a CSV file
    results_df.to_csv(output_path, index=False)
   
    print(results_df)  

def main():    
    getMetrics()
    
if __name__ == '__main__':
    main()