import matplotlib.pyplot as plt

# Fill in names and shooting_num
player_names = [
    "ARES*","AY*","CASH","DG","JEREM","KAZ","MIKE","MOODY","NATHAN","PARKER","RIAZ*","SEB","ELI","THOMAS*"
]

shooting_num = [
    64.00,62.22,48.00,
48.00,
66.00,
60.00,

66.00,
54.00,
50.00,
60.00,
56.00,
50.00,



56.00,
56.00,

]

colors = []
for percentage in shooting_num:
    if percentage >= 72:
        colors.append('green')
    elif percentage >= 55:
        colors.append('yellow')
    else:
        colors.append('red')

plt.figure(figsize=(10, 6))
bars = plt.bar(player_names, shooting_num, color=colors)

plt.title('MARAUDER 50: Efficiencies')
plt.xlabel('Player')
plt.ylabel('Efficiencies')
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
