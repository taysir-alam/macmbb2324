import matplotlib.pyplot as plt
import matplotlib.image as mpimg

court_img = mpimg.imread('courtloc/court.jpg')
fig, ax = plt.subplots()
ax.imshow(court_img)

shot_x = [78,48,113,66,204.6,67,90,76.3,60.3,62,56.5,122.5,76,67,51,533,505,448,553,546,532,553,539,553,446,542,543
    
]

shot_y = [203,151,99,208,129,197,156,197,198,165,334,323,191,165,152,178,185,175,201,194,160,158,210,217,59,212,268.8
    
]


shot_missed_y = [227,223,332,188,335,86,277,38,261,203,177,336,201,200.1,161,207,132,36,230,219,168.7,91.4,36,193,335,188,220,282,37.6,154,187,206.5,163,31,225,213,160,337,214,92,201,203,126.3,154.6,198.9,334,69.7,99,43,85,167,201,214,168,36.7,38,39,208,267,107.4,109,278,38]
shot_missed_x = [74,75,52,84,51,150,45,52.7,199,64,62,60,71,72,60,65,207,54,188.6,61.2,53.6,60,53,56,55,79,67.8,186,80,44,75,58.3,65,42.3,220,547,550,557,536,421,550,551,440,499.9,537,541,450,415,554,423,533,531,539,530,531,534,557,547,417,409.3,413,421,566]

#block_x = [125.6, 275.9, 385.7, 250.2, 160.9]
#block_y = [205.7, 240.8, 215.3, 295.1, 272.4]

turnover_x = [50,39,68,59,42.3,54.6,85,149,107,121.6,103,40,129,476,557,483,529,566,481,521,526,445,488,510,488]
turnover_y = [153,212,340,141,335,104.6,195,332.9,191,192.3,212,215,298,113,291,177,176,34,143,206,150,262,193,48,189]

ax.scatter(shot_x, shot_y, c='green', marker='D', label='Makes')
ax.scatter(shot_missed_x, shot_missed_y, c='red', marker = 'o', label='Misses')
#ax.scatter(block_x, block_y, c='orange', marker='o', label='Blocks')
ax.scatter(turnover_x,turnover_y,c='blue', marker='o', label='Turnovers')

ax.set_xlabel('<-SOUTH Distance from baseline NORTH->')
ax.set_ylabel('<-EAST Distance from sideline WEST->')
ax.set_title('Offense Occurrences v.s. Mohawk')
ax.legend()

plt.show()
