import matplotlib.pyplot as plt
import numpy as np

# Define the range of x values (stake)
x = np.linspace(0, 100, 400)

# Define alpha values
alphas = [4.5, 9.1]

# Colors for each alpha value
style = ['solid', 'dashed',  '#3B4F73']

# Plotting the functions for each alpha
plt.figure(figsize=(10, 6))

for i, alpha in enumerate(alphas):
    # Calculate the values of the functions over the range of x
    linear_values = alpha * x
    square_root_values = alpha * np.sqrt(x)
    log_values = alpha * np.log(x)

    # Plot linear and square root functions with increased line thickness
    plt.plot(x, linear_values, label=r'$w = s$' + f' (α={alpha})', color='#407F7F', linestyle=style[i], linewidth=2)
    plt.plot(x, square_root_values, label=r'$w^* = \sqrt{s}$' + f' (α={alpha})', color='#A67F8E', linestyle=style[i], linewidth=2)
    plt.plot(x, log_values, label=r'$w^\phi = log{s}$' + f' (α={alpha})', color='#3B4F73', linestyle=style[i], linewidth=2)

# Set the plot limits
plt.xlim(0, 100)
plt.ylim(0, max(linear_values.max(), square_root_values.max()))

# Adding labels, title, and grid
plt.xlabel('Stake ($s$)', fontsize=14)
plt.ylabel('Rewards ($r$)', fontsize=14)
plt.legend(fontsize='x-large')
plt.grid(True)

# Show the plot
plt.savefig('tnsm/plots/reward_rate.pdf', format='pdf', dpi=300, transparent=True)
# plt.show()
plt.close()