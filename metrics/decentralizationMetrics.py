import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
import numpy as np


from nakamotoCoefficient import NakamotoCoefficient
from giniCoefficient import GiniCoefficient
from shannonIndex import ShannonIndex
from palma import PalmaRatio
from theilIndex import TheilIndex
from mGammaDeltaModel import mGammaDeltaModel

class DecentralizationMetrics:

    @staticmethod
    def calculate_metrics(date):
        # Define the path to the data folder and the pattern for the date
        data_folder_path = 'data'
        file_pattern = f"{date}_*"

        # Get the list of files for the given date
        files = glob.glob(os.path.join(data_folder_path, file_pattern))

        # Initialize an empty DataFrame to store the results
        results_df = pd.DataFrame(columns=['blockchain', 'N', 'nc_safety', 'nc_safety_percent', 'nc_liveness', 'nc_liveness_percent', 'gini', 'shannon', 'palma', 'theil'])

        mGDModel_df = pd.DataFrame(columns=['blockchain'] + [i for i in range(0, 101, 5)])
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
            shannon = 0 #ShannonIndex.measure(df)
            palma = 0 # PalmaRatio.measure(df)
            theil = 0 # TheilIndex.measure(df)
            
            
            mGDModel_output = mGammaDeltaModel.getDeltaStepFunction(df)

            # Create a new row with the blockchain name and the delta values
            new_row = [blockchain_name] + mGDModel_output

            mGDModel_df = pd.concat([pd.DataFrame([new_row], columns=mGDModel_df.columns), mGDModel_df], ignore_index=True)
            
            results_df = pd.concat([pd.DataFrame([[blockchain_name, len(df), ncSafety, safetyNCPercent, ncLiveness, livenessNCPercent, gini, shannon, palma, theil]], columns=results_df.columns), results_df], ignore_index=True)
        
        return results_df, mGDModel_df
    @staticmethod
    def plot_blockchain_distribution(df):
        """
        Plots the blockchain distribution data.
        
        Parameters:
        df (pandas.DataFrame): DataFrame containing the blockchain data.
        """
        # Transposing the dataframe for plotting
        df_transposed = df.T

        # Ensure all values are numeric, replacing non-numeric values with NaN
        df_transposed = df_transposed.apply(pd.to_numeric, errors='coerce')

        # Convert the index to string to ensure compatibility with matplotlib
        df_transposed.index = df_transposed.index.astype(str)

        # Defining a list of distinct colors for the plot
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange']

        plt.figure(figsize=(12, 8))
        for i, blockchain in enumerate(df_transposed.columns):
            # Handling infinite and non-numeric values for the plot
            y_values = df_transposed[blockchain].replace([np.inf, -np.inf], np.nan)
            plt.plot(df_transposed.index, y_values, label=blockchain, marker='o', color=colors[i % len(colors)])

        # Customizing the plot
        plt.xlabel(r'$\delta$-th percentile validators to richest', fontsize=14)  # x-axis label
        plt.ylabel(r'log($\epsilon$)', fontsize=14)  # y-axis label as log(ε)
        plt.xticks([str(i) for i in range(0, 105, 5)])  # Adjusting x-axis ticks
        plt.yscale('log')  # Using log scale for y-axis
        plt.legend(loc='upper right')
        plt.grid(True)

        # Adjust margins to align '0' on x-axis with y-axis origin
        plt.margins(x=0.02)  # Adjusting x margin

        # Show plot
        plt.show()  
def main():
    # Assume the date is provided as a string in the format 'ddmmyyyy'
    date = '26102023'
    
    # Call the calculate_metrics method to calculate the decentralization metrics
    results_df, mgd_df = DecentralizationMetrics.calculate_metrics(date)
   
    # DecentralizationMetrics.plot_blockchain_distribution(mgd_df)

    
    # Print the results and store them. Used in paper. Date ised 26102023
    # results_df = results_df.drop(columns=['shannon',  'palma',  'theil'])
    # print(results_df)   
    # print(mgd_df)

    # csv_file = f'data/paper/26102023_metrics.csv'
    # mgd_csv = f'data/paper/26102023_mgd.csv'
    # results_df.to_csv(csv_file, index=False)
    # mgd_df.to_csv(mgd_csv,index=False)
if __name__ == '__main__':
    main()