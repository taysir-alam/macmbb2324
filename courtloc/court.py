import matplotlib.pyplot as plt
import matplotlib.image as mpimg

court_img = mpimg.imread('courtloc/court.jpg')
fig, ax = plt.subplots()
ax.imshow(court_img)

shot_x = [78,83,189,163,81,60,53,59.5,195,76,87,533,519,508,546,527,427,521,491,539,524,504,538,528
    
]

shot_y = [157,183,281,309,139,158,177,83,107,206,167,208,223,288,205,218,296,219,179,198,170,198,168,171
    
]


shot_missed_y = [195,200,198,300,216,335,187,208,288,316,103,201,208,293,214,220,316,331,152,223,202,149,30,90,89,219,149,187,159,39,108,198,286,204,214,198,136,234,205,195,202,185,341,239,329,118,304]
shot_missed_x = [65,220,87,179,51,75,77,57,194,175,208,136,41,164,145,125,125,42,46,230,66,94,40,179,139,213,429,510,538,562,440,519,413,391,533,558,385,510,540,522,545,372,545,440,505,401,443]

#block_x = [125.6, 275.9, 385.7, 250.2, 160.9]
#block_y = [205.7, 240.8, 215.3, 295.1, 272.4]
#misplay_x = [43.4,93,123]
#misplay_y = [247.5,197,187]

turnover_x = [199,183,94,68,454,514,418,527]
turnover_y = [191,256,224,194,220,82,207,149]

#ax.scatter(misplay_x, misplay_y, c='purple', marker='D', label='Misplays')
ax.scatter(shot_x, shot_y, c='green', marker='D', label='Makes')
ax.scatter(shot_missed_x, shot_missed_y, c='red', marker = 'o', label='Misses')
#ax.scatter(block_x, block_y, c='orange', marker='o', label='Blocks')
ax.scatter(turnover_x,turnover_y,c='blue', marker='o', label='Turnovers')

ax.set_xlabel('<-SOUTH Distance from baseline NORTH->')
ax.set_ylabel('<-EAST Distance from sideline WEST->')
ax.set_title('Offense Occurrences v.s. Memorial')
ax.legend()

plt.show()
