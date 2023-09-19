import matplotlib.pyplot as plt
import numpy as np

# FILL IN NAMES AND STATS ACROSS A WEEK (or greater sample)
data = {
    "NAME": [],
    "9/11/2023": [21.00],
    "9/12/2023": [13.00],
    "9/13/2023": [16.00, 24.00, None, None, 25.00, 25.00, 25.00, 20.00, None, 20.00, 25.00, 20.00, 6.00, 20.00, None, None, None, None, None],
    "9/14/2023": [21.00, None, 12.00, 25.00, 21.00, 21.00, 25.00, 18.00, 25.00, 25.00, 24.00, 20.00, 14.00, 21.00, 19.00, None, 21.00, 24.00, 21.00]
}


fig, ax = plt.subplots(figsize=(10, 8))

for i, name in enumerate(data["NAME"]):
    y_values = [data[date][i] for date in data.keys() if date != "NAME"]
    x_values = [date for date in data.keys() if date != "NAME"]
    label = name
    linestyle = '-' if all(val is not None for val in y_values) else '--'
    ax.plot(x_values, y_values, label=label, linestyle=linestyle, marker='o')


ax.set_ylim(5, 30)  
ax.set_yticks(np.arange(0, 26, 5))  
ax.set_xlabel("Session Date")
ax.set_title("WEEK 2: 25 IN 2 PROGRESSION")
ax.legend(loc='upper right')
plt.grid(True)

plt.tight_layout()
plt.show()

