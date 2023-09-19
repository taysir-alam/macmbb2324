import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

player_names =  ["NATHAN","RIAZ", "PARKER", "JEREMIAH", "MOODY", "KAZIM", "MATT", "ARES", "SEB", "DANIEL", "THOMAS"]
shooting_percentages = [31, 21, 24, 33, 28, 28, 27, 24, 23, 22, 9]


colors = []
for percentage in shooting_percentages:
    if percentage >= 28:
        colors.append('green')
    elif percentage >= 21:
        colors.append('yellow')
    else:
        colors.append('red')

plt.figure(figsize=(10, 6))
bar = plt.bar(player_names, shooting_percentages, color=colors)

plt.title('30 IN 2:30')
plt.xlabel('Player')
plt.ylabel('Shooting Percentage')
plt.xticks(rotation=90)
plt.ylim(0, 30)  


for bar, percentage in zip(bar, shooting_percentages):
    if percentage <= 29:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5, f'{percentage}', ha='center')


plt.tight_layout()
plt.show()
