import matplotlib.pyplot as plt

# Fill in names and shooting_num
player_names = [
    "ARES", "CASH", "DG", "JEREM", "KAZ", "MIKE",
    "MOODY", "PARKER", "RIAZ", "SEB", "TYRELLE", "ELI", "THOMAS"
]

shooting_num = [
    58, 71, 43, 55, 71, 66, 69,
    55, 21, 51, 71, 63, 56
]

colors = []
for percentage in shooting_num:
    if percentage >= 70:
        colors.append('green')
    elif percentage >= 40:
        colors.append('yellow')
    else:
        colors.append('red')

plt.figure(figsize=(10, 6))
bars = plt.bar(player_names, shooting_num, color=colors)

plt.title('25 IN 2: Efficiencies')
plt.xlabel('Player')
plt.ylabel('Shooting Efficiency')
plt.xticks(rotation=45, ha="right")
plt.ylim(0, 100)

for bar, percentage in zip(bars, shooting_num):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.02,
        f'{percentage:.2f}',  # Format the percentage to two decimal places
        ha='center',
        va='bottom'
    )

plt.tight_layout()
plt.show()
