import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = "data/paper/02122023_aptos_proposals.csv"
df = pd.read_csv(file_path)

# Assuming 'proposals' and 'tokens' columns exist in your dataframe
total_proposals = df['proposals'].sum()
total_weight = df['tokens'].sum()

df['proposals_expected'] = round((df['tokens']/total_weight) * total_proposals, 2)

df['srsw'] = np.sqrt(df['tokens'])
srsw_weight = df['srsw'].sum()
df['proposals_srsw'] = round((df['srsw']/srsw_weight) * total_proposals, 2)

# Plotting with specified colors
plt.plot(df['tokens'], df['proposals'], label='proposals observed', color='#407F7F')
plt.plot(df['tokens'], df['proposals_expected'], label='proposals predicted', color='red')
plt.plot(df['tokens'], df['proposals_srsw'], label='proposals SRSW', color='#B26670')

plt.xlabel('Stake ($s$)')
plt.ylabel('Number of Proposals')
plt.legend(fontsize='large')

plt.savefig('data/paper/proposals_srsw.pdf', transparent=True)

plt.show()

