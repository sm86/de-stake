import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
import numpy as np


from nakamotoCoefficient import NakamotoCoefficient
from giniCoefficient import GiniCoefficient
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
        results_df = pd.DataFrame(columns=['blockchain', 'm', 'G', 'nL', 'nLP', 'nS', 'nSP', 'srsw_G', 'srsw_nL', 'srsw_nLP', 'srsw_nS', 'srsw_nSP'])

        # Loop through each file, calculate the metrics, and append the results to the results_df
        for file in files:
            # Extract the blockchain name from the file name
            blockchain_name = os.path.basename(file).split('_')[1].split('.')[0]
            # Load the CSV file into a DataFrame
            df = pd.read_csv(file)

            srsw_df = df.copy()
            srsw_df['tokens'] = np.sqrt(srsw_df['tokens'])

            # Calculate the Nakamoto and Gini Coefficients
            ncSafety, safetyNCPercent = NakamotoCoefficient.measureSafetyNC(df)
            ncLiveness, livenessNCPercent = NakamotoCoefficient.measureLivenessNC(df)
            gini = GiniCoefficient.measure(df)

            # Calculate the Nakamoto and Gini Coefficients
            srsw_ncSafety, srsw_safetyNCPercent = NakamotoCoefficient.measureSafetyNC(srsw_df)
            srsw_ncLiveness, srsw_livenessNCPercent = NakamotoCoefficient.measureLivenessNC(srsw_df)
            srsw_gini = GiniCoefficient.measure(srsw_df)

            results_df = pd.concat([pd.DataFrame([[blockchain_name, len(df), gini, ncLiveness, livenessNCPercent, ncSafety, safetyNCPercent, srsw_gini, srsw_ncLiveness, srsw_livenessNCPercent, srsw_ncSafety, srsw_safetyNCPercent]], columns=results_df.columns), results_df], ignore_index=True)
            results_df = results_df.sort_values(by='blockchain')
        return results_df
def plot(df):
    plt.figure(figsize=(10, 5))
    df[['G', 'srsw_G']].plot(kind='bar', color=['#407F7F', '#A67F8E'])
    plt.xticks(range(len(df['blockchain'])), df['blockchain'], rotation=10)
    plt.ylabel('Gini Index '+ r'($G$)')
    plt.legend(["$w=s$", "SRSW"], fontsize='large')

    # Adding grid lines
    plt.grid(True, axis='y')
    # Save the figure to a file
    plt.savefig('data/paper/gini_index_comparison.pdf', transparent=True)
    # Show the plot
    # plt.show()
    
    # Settings for the grouped bar chart
    bar_width = 0.2
    index = np.arange(len(df['blockchain']))

    # Creating the plot
    plt.figure(figsize=(12, 6))

    # Updated color palette - more muted, professional tones
    colors = ['#72B184', '#B26670', '#407F7F', '#A67F8E']  # Muted green, muted red, teal, soft purple

    # Nakamoto Coefficient Liveness
    plt.bar(index - bar_width/2, df['nLP'], bar_width, label=r'$w=s \quad \rho_{\mathbb{N}_L}$', color=colors[0])
    plt.bar(index + bar_width/2, df['srsw_nLP'], bar_width, label='SRSW ' + r'$\rho_{\mathbb{N}_L}$', color=colors[1])

    # Nakamoto Coefficient Safety
    plt.bar(index + 1.5 * bar_width, df['nSP'], bar_width, label=r'$w=s \quad \rho_{\mathbb{N}_S}$', color=colors[2])
    plt.bar(index + 2.5 * bar_width, df['srsw_nSP'], bar_width, label='SRSW ' + r'$\rho_{\mathbb{N}_S}$', color=colors[3])

    # Adding labels and title
    plt.xlabel('Blockchain')
    plt.ylabel('Nakamoto Coefficients % ' + r'$(\rho_{\mathbb{N}}$)')
    plt.xticks(index + bar_width, df['blockchain'])

    # Increase legend size
    plt.legend(fontsize='large')

    # Adding grid lines
    plt.grid(True, axis='y')

    # Save the figure to a file
    plt.savefig('data/paper/nakamoto_coefficients_combined.pdf', transparent=True)

    # Show the plot
    plt.show()

    

def main():
    # Assume the date is provided as a string in the format 'ddmmyyyy'
    date = '26102023'
    
    # Call the calculate_metrics method to calculate the decentralization metrics
    results_df = DecentralizationMetrics.calculate_metrics(date)
    # plot(results_df)
    
    print(results_df)   
    

    results_df['G_inc'] = (results_df['G'] - results_df['srsw_G'])/results_df['G'] * 100
    results_df['nL_inc'] = (results_df['srsw_nL'] - results_df['nL'])/results_df['nL'] * 100
    results_df['nS_inc'] = (results_df['srsw_nS'] - results_df['nS'])/results_df['nS'] * 100
    
    print(results_df)
    print(results_df['G_inc'].mean())
    print(results_df['nL_inc'].mean())
    print(results_df['nS_inc'].mean())
    # csv_file = f'data/paper/26102023_metrics.csv'
    # mgd_csv = f'data/paper/26102023_mgd.csv'
    # results_df.to_csv(csv_file, index=False)
    # mgd_df.to_csv(mgd_csv,index=False)
if __name__ == '__main__':
    main()