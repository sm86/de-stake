import matplotlib.pyplot as plt
import numpy as np

# Define the range of x values (stake)
x = np.linspace(0, 100, 400)

# Define alpha values
alphas = [4.5, 9.1]

# Colors for each alpha value
colors = ['#407F7F', '#A67F8E']

# Plotting the functions for each alpha
plt.figure(figsize=(10, 6))

for i, alpha in enumerate(alphas):
    # Calculate the values of the functions over the range of x
    linear_values = alpha * x
    square_root_values = alpha * np.sqrt(x)

    # Plot linear and square root functions with increased line thickness
    plt.plot(x, linear_values, label=r'$w = s$' + f' (α={alpha})', color=colors[i], linestyle='solid', linewidth=2)
    plt.plot(x, square_root_values, label=r'$w^* = \sqrt{s}$' + f' (α={alpha})', color=colors[i], linestyle='dashed', linewidth=2)

# Set the plot limits
plt.xlim(0, 100)
plt.ylim(0, max(linear_values.max(), square_root_values.max()))

# Adding labels, title, and grid
plt.xlabel('Stake ($s$)', fontsize=14)
plt.ylabel('Rewards ($r$)', fontsize=14)
plt.legend(fontsize='x-large')
plt.grid(True)

# Show the plot
plt.savefig('data/paper/reward_rate.pdf', transparent=True)
plt.show()