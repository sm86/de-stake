import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns

class ShapleyGini:

    @staticmethod
    def calculate_shapley(df, col, liveness_ratio=0.33, safety_ratio=0.66, num_samples=10000):
        weights = df[col].to_numpy()
        total_weight = weights.sum()
        n = len(weights)

        shapley_values_liveness = np.zeros(n)
        shapley_values_safety = np.zeros(n)
        
        # Monte Carlo sampling to approximate Shapley values
        for i in range(n):
            marginal_contributions_liveness = []
            marginal_contributions_safety = []
            
            # Sample random subsets to approximate the Shapley values
            for _ in range(num_samples):
                subset = random.sample([j for j in range(n) if j != i], k=random.randint(0, n - 1))
                subset_sum = weights[subset].sum()
                
                # Liveness marginal contribution
                if subset_sum <= liveness_ratio * total_weight and (subset_sum + weights[i]) > liveness_ratio * total_weight:
                    marginal_contributions_liveness.append(1)
                else:
                    marginal_contributions_liveness.append(0)

                # Safety marginal contribution
                if subset_sum <= safety_ratio * total_weight and (subset_sum + weights[i]) > safety_ratio * total_weight:
                    marginal_contributions_safety.append(1)
                else:
                    marginal_contributions_safety.append(0)
            
            # Average the marginal contributions
            shapley_values_liveness[i] = np.mean(marginal_contributions_liveness)
            shapley_values_safety[i] = np.mean(marginal_contributions_safety)

        return shapley_values_liveness, shapley_values_safety

    @staticmethod
    def gini_coefficient(values):
        values_sorted = np.sort(values)
        n = len(values_sorted)

        # Gini calculation based on cumulative distribution
        cumulative_sum = np.cumsum(values_sorted, dtype=np.float64)
        gini_numerator = np.sum((2 * np.arange(1, n + 1) - n - 1) * values_sorted)
        gini_denominator = n * cumulative_sum[-1]  # Total sum of values

        gini_index = gini_numerator / gini_denominator
        return round(gini_index, 3)

    @staticmethod
    def measure(df, col='tokens'):
        # Calculate both liveness and safety Shapley values in one pass
        shapley_liveness, shapley_safety = ShapleyGini.calculate_shapley(df, col, liveness_ratio=0.33, safety_ratio=0.66, num_samples=10000)
        
        # Method 1: Using numpy
        correlation = np.corrcoef(shapley_liveness, shapley_safety)[0, 1]
        print(f'Correlation coefficient (numpy): {correlation:.2f}')

        # Method 1: Using numpy
        correlation = np.corrcoef(df['tokens'], shapley_safety)[0, 1]
        print(f'Correlation coefficient with Stake and shapley_safety: {correlation:.2f}')
        
        # Method 1: Using numpy
        correlation = np.corrcoef(df['tokens'], shapley_liveness)[0, 1]
        print(f'Correlation coefficient with Stake and shapley_liveness: {correlation:.2f}')
        
        # ShapleyGini.plot_density(shapley_liveness, shapley_safety)
        
        # Calculate Gini coefficients for liveness and safety
        gini_liveness = ShapleyGini.gini_coefficient(shapley_liveness)
        gini_safety = ShapleyGini.gini_coefficient(shapley_safety)

        return gini_liveness, gini_safety, correlation

    @staticmethod
    def plot_density(arr1, arr2, label1='liveness', label2='safety', title='Density Plot'):
        """
        Plots density plots for two arrays to visualize their distributions.
        
        Parameters:
        arr1: array-like
            First array for plotting.
        arr2: array-like
            Second array for plotting.
        label1: str
            Label for the first array.
        label2: str
            Label for the second array.
        title: str
            Title for the plot.
        """
        # Create density plots
        sns.kdeplot(arr1, label=label1, shade=True, alpha=0.6)
        sns.kdeplot(arr2, label=label2, shade=True, alpha=0.6)
        
        # Add labels and title
        plt.xlabel('Value')
        plt.ylabel('Density')
        plt.title(title)
        plt.legend()
        plt.grid(True)
        
        # Show the plot
        plt.show()

def main():
    # Load the CSV file into a DataFrame
    file_path = 'data/25102023_sui.csv'  # Replace with the path to your CSV file
    df = pd.read_csv(file_path)
    
    # Calculate Shapley values and Gini coefficients for Liveness and Safety
    gini_liveness, gini_safety = ShapleyGini.measure(df)
    
    
    
    print("Shapley Values and Gini Coefficients:")
    print("Liveness Gini Coefficient:", gini_liveness)
    print("Safety Gini Coefficient:", gini_safety)

if __name__ == '__main__':
    main()