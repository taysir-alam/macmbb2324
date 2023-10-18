import matplotlib.pyplot as plt

# Fill in names and shooting_num
player_names = [
    "ARES", "AY", "BA", "CASH", "DG", "JEREM", "KAZ", "MATT", "MOODY", "NATHAN", "PARKER", "RIAZ", "SEB", "STEVO", "TYRELLE", "ELI"
]

shooting_num = [
    58.00, 70.00, 58.00, 70.00, 54.00, 60.00, 64.00, 44.00, 74.00, 50.00, 68.00, 52.00, 60.00, 64.00, 64.00, 52.00
]

colors = []
for percentage in shooting_num:
    if percentage >= 68:
        colors.append('green')
    elif percentage >= 52:
        colors.append('yellow')
    else:
        colors.append('red')

plt.figure(figsize=(10, 6))
bars = plt.bar(player_names, shooting_num, color=colors)

plt.title('MARAUDER 50: October 12th')
plt.xlabel('Player')
plt.ylabel('TOTALS')
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
