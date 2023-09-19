import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

player_names = ["NATHAN C", "STEVO*", "RIAZ", "PARKER", "JEREMIAH", "MOODY", "KAZIM", "MATT", "ARES", "ELIJAH", "SEB", "DANIEL", "THOMAS", "BA*", "AY"]
shooting_percentages = [8, 12, 12, 11, 14, 15, 15, 2.5, 9.5, 12, 13, 12.5, 7.5, 3, 13.5]

colors = []
for percentage in shooting_percentages:
    if percentage >= 15:
        colors.append('green')
    elif percentage >= 8:
        colors.append('yellow')
    else:
        colors.append('red')

plt.figure(figsize=(10, 6))
bars = plt.bar(player_names, shooting_percentages, color=colors)

plt.title('ROLLING AVERAGE: 3 IN A ROW')
plt.xlabel('Player')
plt.ylabel('Shooting Percentage')
plt.xticks(rotation=90)
plt.ylim(0, 15) 

for bar, percentage in zip(bars, shooting_percentages):
    if percentage <= 14:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5, f'{percentage}', ha='center')

    


plt.tight_layout()
plt.show()
