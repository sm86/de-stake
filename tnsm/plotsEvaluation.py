import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
import numpy as np


def plot_gini(df):
    plt.figure(figsize=(10, 5))
    df[['gini_tokens', 'gini_srsw', 'gini_lsw']].plot(kind='bar', color=['#407F7F', '#A67F8E', '#3B4F73'])
    plt.xticks(range(len(df['blockchain'])), df['blockchain'].str.capitalize(), rotation=20, fontsize=11)
    plt.ylabel('Gini Index '+ r'($G$)', fontsize=14)
    plt.legend(["$w=s \quad G$", "SRSW " +r'$G^*$',"LSW " +r'$G^\phi$'], fontsize=13,loc='upper left')

    # Adding grid lines
    plt.grid(True, axis='y',linewidth=0.5, alpha=0.7)
    # Save the figure to a file
    plot_file_path = os.path.join('tnsm/plots/' f'gini_results.pdf')  # Save as PDF
    plt.savefig(plot_file_path, format='pdf', dpi=300, transparent=True)
    plt.close()  # Close the plot to free memory

    print(f'Saved plot to {plot_file_path}')
    


def plot_zipfs(df):
    plt.figure(figsize=(10, 5))
    ax = df[['zipfs_tokens', 'zipfs_srsw', 'zipfs_lsw']].plot(
        kind='bar', color=['#407F7F', '#A67F8E', '#3B4F73'], figsize=(10, 5)
    )
    
    # Setting the y-axis cap
    ax.set_ylim(0, 3.6)  # Cap y-axis slightly above the highest non-Celestia value
    
    # Annotate Celestia's high value within the bar
    # Annotate Celestia's high value within the bar
    celestia_index = df[df['blockchain'].str.lower() == 'celestia'].index[0]
    high_value = df.loc[celestia_index, 'zipfs_tokens']
    ax.annotate(f'{high_value:.2f}', 
                xy=(celestia_index, 2),  # Position lower inside the bar
                xytext=(celestia_index, 3.2),  # Place text at 2.5 for more visibility
                ha='center', color='black', fontsize=10)  # Larger font and bold


    # Setting labels, legend, and grid
    plt.xticks(range(len(df['blockchain'])), df['blockchain'].str.capitalize(), rotation=0, fontsize=12)
    plt.ylabel('Zipf\'s Coefficient '+ r'($\mathcal{Z}$)', fontsize=14)
    plt.legend(["$w=s \quad \mathcal{Z}$", "SRSW " + r'$\mathcal{Z}^*$', "LSW " + r'$\mathcal{Z}^\phi$'], fontsize=13, loc='upper right')
    plt.grid(True, axis='y', linewidth=0.5, alpha=0.7)
    
    # Save the figure
    plot_file_path = os.path.join('tnsm/plots/', 'zipfs_analysis.pdf')
    plt.savefig(plot_file_path, format='pdf', dpi=300, transparent=True)
    plt.close()

    print(f'Saved plot to {plot_file_path}')

    
def plot_nakamoto(df):
    # Settings for the grouped bar chart
    bar_width = 0.15  # Adjusted to fit 6 bars within each blockchain group
    index = np.arange(len(df['blockchain']))

    # Creating the plot
    plt.figure(figsize=(14, 7))

    # Updated color palette to have distinct colors for each type
    colors = ['#72B184', '#B26670', '#407F7F', '#A67F8E', '#4C6A92', '#3B4F73']  # Muted green, muted red, teal, soft purple, gold, violet 4C6A92

    # Nakamoto Coefficient Liveness
    plt.bar(index - 2.5 * bar_width, df['nc_liveness_tokens'], bar_width, label=r'$w=s \quad \rho_{N_L}$', color=colors[0])
    plt.bar(index - 1.5 * bar_width, df['nc_liveness_srsw'], bar_width, label='SRSW ' + r'$\rho_{N_L^*}$', color=colors[1])
    plt.bar(index - 0.5 * bar_width, df['nc_liveness_lsw'], bar_width, label='LSW ' + r'$\rho_{N_L}^{\phi}$', color=colors[4])

    # Nakamoto Coefficient Safety
    plt.bar(index + 0.5 * bar_width, df['nc_safety_tokens'], bar_width, label=r'$w=s \quad \rho_{N_S}$', color=colors[2])
    plt.bar(index + 1.5 * bar_width, df['nc_safety_srsw'], bar_width, label='SRSW ' + r'$\rho_{N_S^*}$', color=colors[3])
    plt.bar(index + 2.5 * bar_width, df['nc_safety_lsw'], bar_width, label='LSW ' + r'$\rho_{N_S}^{\phi}$', color=colors[5])

    # Adding labels and title
    plt.ylabel('Nakamoto Coefficients' + r'$(\rho_{N_L}, \rho_{N_S}$)', fontsize=18)
    plt.xticks(index, df['blockchain'].str.capitalize(), fontsize=18)

    # Increase legend size and place it outside the plot
    plt.legend(fontsize='large', loc='upper left')

    # Adding grid lines
    plt.grid(True, axis='y', linewidth=0.5, alpha=0.7)

    # Show the plot
    plt.tight_layout()

    plot_file_path = os.path.join('tnsm/plots/' f'nakamoto_analysis.pdf')  # Save as PDF
    plt.savefig(plot_file_path, format='pdf', dpi=300, transparent=True)
    plt.close()  # Close the plot to free memory

    print(f'Saved plot to {plot_file_path}')

def reshapeDF(df):
    # Filter out rows with 'tokens' as scale, as only srsw and lsw are needed in the new structure
    df_filtered = df[df['scale'].isin(['tokens', 'srsw', 'lsw'])]

    # Pivot the DataFrame to get separate columns for each 'scale' type with suffixes for each metric
    df_pivot = df_filtered.pivot(index=['blockchain', 'N'], columns='scale', 
                                values=['nc_safety', 'nc_liveness', 'gini', 'hhi', 
                                        'shapley_liveness', 'shapley_safety', 'zipfs'])

    # Flatten the multi-level columns and rename them to match the desired format
    df_pivot.columns = [f"{metric}_{scale}" for metric, scale in df_pivot.columns]

    # Reset index to turn the multi-index back into columns
    df_pivot.reset_index(inplace=True)

    return df_pivot
   

def main():
    # Assume the date is provided as a string in the format 'ddmmyyyy'
    file_path = 'tnsm/results/empiricial-analysis-tnsm.csv'  # Replace with the path to your CSV file
    df = pd.read_csv(file_path)
    df = reshapeDF(df)
    
    df.to_csv('tnsm/results/reshaped-empiricial-analysis-tnsm.csv', index=False)

    # print(df)
    # plot_nakamoto(df)
    # plot_gini(df)
    # plot_zipfs(df)

    # results_df['G_inc'] = (results_df['G'] - results_df['srsw_G'])/results_df['G'] * 100
    # results_df['nL_inc'] = (results_df['srsw_nL'] - results_df['nL'])/results_df['nL'] * 100
    # results_df['nS_inc'] = (results_df['srsw_nS'] - results_df['nS'])/results_df['nS'] * 100
    
    # print(results_df)
    # print(results_df['G_inc'].mean())
    # print(results_df['nL_inc'].mean())
    # print(results_df['nS_inc'].mean())
    # csv_file = f'data/paper/14122023_metrics.csv'
    # # mgd_csv = f'data/paper/14122023_mgd.csv'
    # results_df.to_csv(csv_file, index=False)
    # # mgd_df.to_csv(mgd_csv,index=False)
if __name__ == '__main__':
    main()