import matplotlib.pyplot as plt
import matplotlib.image as mpimg

court_img = mpimg.imread('courtloc/court.jpg')
fig, ax = plt.subplots()
ax.imshow(court_img)

shot_x = [
    60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
    70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
    80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
    90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
    100, 61, 62, 63, 64, 65, 66, 67, 68, 69,
    70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
    80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
    90, 91, 92, 93, 94, 95, 96,75,80, 85,150,164,57,219,78,177
]

shot_y = [
    192, 173, 206, 213, 167, 179, 203, 158, 203, 202,
    219, 173, 199, 209, 192, 208, 158, 175, 162, 152,
    216, 174, 186, 196, 222, 165, 222, 158, 188, 163,
    196, 222, 217, 152, 181, 188, 154, 191, 154, 204,
    157, 171, 214, 163, 160, 209, 185, 208, 205, 210,
    153, 153, 160, 212, 170, 220, 209, 182, 155, 161,
    173, 161, 186, 178, 194, 172, 176, 152, 169, 196,
    180, 163, 180, 170, 178, 203, 177,49,47,51,241,303,330,184,340,78
]


shot_missed_y = [346, 336, 345, 342, 332, 334,294,36,49,45,44,200,338,350,78,204,90,153,182,313,237,199]
shot_missed_x = [85, 101, 69, 97, 76, 104,175,52,41,47,61,99,50,45,205,220,183,226,230,159,210,230]

#block_x = [125.6, 275.9, 385.7, 250.2, 160.9]
#block_y = [205.7, 240.8, 215.3, 295.1, 272.4]

turnover_x = [210,100,44]
turnover_y = [275,175,175]

ax.scatter(shot_x, shot_y, c='green', marker='.', label='Makes')
ax.scatter(shot_missed_x, shot_missed_y, c='red', marker = 'D', label='Misses')
#ax.scatter(block_x, block_y, c='orange', marker='o', label='Blocks')
ax.scatter(turnover_x,turnover_y,c='blue', marker='o', label='Turnovers')

ax.set_xlabel('Distance from baseline')
ax.set_ylabel('Distance from sideline')
ax.set_title('Occurrence Locations 09/22/2023')
ax.legend()

plt.show()
