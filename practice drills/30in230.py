import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

player_names =  ["ARES","AY","NATHAN", "PARKER", "SEB", "STEVO"]
shooting_percentages = [60.98, 58.82, 52.63, 59.57, 52.38, 60.98]


colors = []
for percentage in shooting_percentages:
    if percentage >= 75:
        colors.append('green')
    elif percentage >= 45:
        colors.append('yellow')
    else:
        colors.append('red')

plt.figure(figsize=(10, 6))
bar = plt.bar(player_names, shooting_percentages, color=colors)

plt.title('30 IN 2:30 - October 16th (FIRST SET)')
plt.xlabel('Player')
plt.ylabel('Shooting Percentage')
plt.xticks(rotation=90)
plt.ylim(0, 100)  


for bar, percentage in zip(bar, shooting_percentages):
    if percentage <= 100.00:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5, f'{percentage}', ha='center')


plt.tight_layout()
plt.show()
