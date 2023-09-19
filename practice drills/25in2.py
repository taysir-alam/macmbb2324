import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# FILL IN NAMES AND SHOOTING_NUM
player_names = ["ARES",
"AY",
"BA",
"CASH",
"DG",
"JEREM",
"KAZ",
"MATT",
"MIKE",
"MOODY",
"NATHAN",
"PARKER",
"RIAZ",
"SEB",
"STEVO",
"TYRELLE",
"ELI",
"THOMAS"
]
# shooting_num91223 = [19, 15, 16, 25, 25, 17, 24, 17, 13, 22, 20, 20, 22, 14, 20]
shooting_num = [17.75,
24.00,
15.00,
25.00,
21.75,
22.75,
24.50,
17.50,
22.00,
20.50,
20.50,
19.75,
12.00,
22.00,
19.33,
21.00,
24.00,
21.00
]

colors = []
for percentage in shooting_num:
    if percentage >= 22:
        colors.append('green')
    elif percentage >= 16:
        colors.append('yellow')
    else:
        colors.append('red')

plt.figure(figsize=(10, 6))
bars = plt.bar(player_names, shooting_num, color=colors)

plt.title('ROLLING AVERAGE:25 IN 2 MINUTES')
plt.xlabel('Player')
plt.ylabel('Shooting Numbers')
plt.xticks(rotation=90)
plt.ylim(0, 25)  

for bar, percentage in zip(bars, shooting_num):
    if percentage <= 24:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5, f'{percentage}', ha='center')

plt.tight_layout()
plt.show()
