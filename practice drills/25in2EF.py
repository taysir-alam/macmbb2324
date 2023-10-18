import matplotlib.pyplot as plt

# Fill in names and shooting_num
player_names = ["AY", "ELIJAH", "MATT", "MOODY", "NATE", "PARKER", "SEB", "STEVO","TYLER"]

shooting_num = [
    75.76, 56.82, 47.22, 65.71, 45.45, 51.22, 63.16, 18.75, 62.50
]

colors = []
for percentage in shooting_num:
    if percentage >= 70:
        colors.append('#4CAF50')  # Green
    elif percentage >= 40:
        colors.append('#FFFF00')  # Yellow
    else:
        colors.append('#F44336')  # Red

plt.figure(figsize=(12, 6))
bars = plt.bar(player_names, shooting_num, color=colors)

plt.title('25 in 2 Eff - October 17th (2nd Set)', fontsize=16, fontweight='bold')
plt.xlabel('Player', fontsize=12)
plt.ylabel('Shooting Efficiency (%)', fontsize=12)
plt.xticks(rotation=45, ha="right", fontsize=10)
plt.ylim(0, 100)

for bar, percentage in zip(bars, shooting_num):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 2,
        f'{percentage:.2f}%',  # Format the percentage to two decimal places
        ha='center',
        va='bottom',
        fontsize=10
    )

plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
