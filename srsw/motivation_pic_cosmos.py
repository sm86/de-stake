import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
aptos_df = pd.read_csv('data/04122023_aptos.csv')
cosmos_df = pd.read_csv('data/04122023_cosmos.csv')
# Plot the line graph
plt.plot(cosmos_df.index, cosmos_df['tokens'], label='Cosmos')

# Customize the plot
plt.xlabel('Index')
plt.ylabel('Tokens')
plt.title('Staked Tokens Distribution Among Cosmos Validators')
plt.legend()

# Show the plot
plt.show()
