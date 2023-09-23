import matplotlib.pyplot as plt

# Fill in names and shooting_num
player_names = [
    "ARES","AY","CASH","DG","JEREM","KAZ","MIKE","MOODY","NATHAN","PARKER","RIAZ","SEB","ELI","THOMAS"
]

shooting_num = [
    32,28,34,24,33,30,33,27,25,30,28,25,28,28
]

colors = []
for percentage in shooting_num:
    if percentage >= 34:
        colors.append('green')
    elif percentage >= 26:
        colors.append('yellow')
    else:
        colors.append('red')

plt.figure(figsize=(10, 6))
bars = plt.bar(player_names, shooting_num, color=colors)

plt.title('MARAUDER 50')
plt.xlabel('Player')
plt.ylabel('TOTALS')
plt.xticks(rotation=45, ha="right")
plt.ylim(0, 50)

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
