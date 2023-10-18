import matplotlib.pyplot as plt
import numpy as np

player_names = ["ARES", "BA", "CASH", "DG", "JEREM", "KAZ", "MOODY", "NATHAN", "PARKER", "RIAZ", "SEB", "STEVO", "ELIJAH"]
shooting_percentages2 = [61.00, 43.00, 53.00, 51.00, 46.00, 53.85,0, 67.00, 59.00, 44.00, 58.00, 51.00, 51.00]  # Added 0 for MOODY
shooting_percentages1 = [60.00, 42.00, 51.16, 65.91, 46.30, 64.81, 53.00, 58.00, 62.00, 50.00, 59.00, 50.00, 53.00]

x = np.arange(len(player_names))  # X-axis positions for players
width = 0.35  # Width of the bars

fig, ax = plt.subplots()
bars1 = ax.bar(x - width/2, shooting_percentages1, width, label='Shooting Percentages 1', color='g')
bars2 = ax.bar(x + width/2, shooting_percentages2, width, label='Shooting Percentages 2', color='g')

# Color coding based on the percentages
for i in range(len(player_names)):
    if shooting_percentages1[i] < 35 or shooting_percentages2[i] < 35:
        bars1[i].set_color('r')
        bars2[i].set_color('r')
    elif 35 <= shooting_percentages1[i] <= 70 or 35 <= shooting_percentages2[i] <= 70:
        bars1[i].set_color('y')
        bars2[i].set_color('y')

ax.set_xlabel('Players')
ax.set_ylabel('Shooting Percentages')
ax.set_title('Double Bar Graph of Shooting Percentages')
ax.set_xticks(x)
ax.set_xticklabels(player_names)
ax.legend()

plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()

plt.show()
