import matplotlib.pyplot as plt
import matplotlib.image as mpimg

court_img = mpimg.imread('courtloc/court.jpg')
fig, ax = plt.subplots()
ax.imshow(court_img)

shot_x = [112.5, 187.3, 398.2, 240.6, 127.9, 312.4, 193.7, 288.2, 365.9, 146.7, 327.5, 219.1, 362.0]
shot_y = [214.8, 242.7, 177.1, 300.3, 265.5, 145.2, 318.9, 246.8, 185.7, 237.4, 201.9, 320.7, 180.5]

shot_missed_x = [210.0, 260.7, 330.5, 380.1, 220.8, 140.2, 335.6, 200.4, 298.9]
shot_missed_y = [225.3, 255.4, 375.9, 198.7, 310.2, 275.1, 155.6, 325.7, 235.8]

block_x = [125.6, 275.9, 315.4, 385.7, 250.2, 160.9]
block_y = [205.7, 240.8, 385.6, 215.3, 295.1, 272.4]

turnover_x = [240.5, 190.3, 310.8, 400.0, 268.7, 150.4]
turnover_y = [280.6, 265.2, 390.0, 175.7, 305.8, 248.9]

ax.scatter(shot_x, shot_y, c='red', marker='o', label='Makes')
ax.scatter(shot_missed_x, shot_missed_y, c='blue', marker = 'o', label='Misses')
ax.scatter(block_x, block_y, c='green', marker='o', label='Blocks')
ax.scatter(turnover_x,turnover_y,c='pink', marker='o', label='Turnovers')

ax.set_xlabel('Distance from baseline')
ax.set_ylabel('Distance from sideline')
ax.set_title('Basketball Game Shot Locations')
ax.legend()

plt.show()
