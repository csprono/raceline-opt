import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from scipy import interpolate

track = cv.imread(r'src\centreline_gen\output\hockenheim_widths.png',cv.IMREAD_GRAYSCALE)

def extract_centres(img:np.ndarray):
    visited = {}
    stack = []
    directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    centreline = []
    

    start_y = img.shape[1] // 2 - 120
    start_x = 0
    while img[start_x][start_y] == 0.0:
        start_x += 1
    
    start_point = (start_x,start_y)


    stack.append(start_point)
    while stack:
        point = stack.pop()
        if point not in visited:
            visited[point] = True
            centreline.append(point)
            for vec in directions:
                new_point = (point[0]+vec[0],point[1]+vec[1])
                if img[new_point[0],new_point[1]] != 0.0 and new_point not in visited:
                    stack.append(new_point)

    return centreline

centreline = np.array(extract_centres(track))



centreline = np.vstack([centreline, centreline[0]])

x = centreline[::,0]
y = centreline[::,1]

tck,u = interpolate.splprep([x,y], s=0,per=True)
xi, yi = interpolate.splev(np.linspace(0, 1, 1000), tck)

# plot the result
fig, ax = plt.subplots(1, 1)
ax.plot(x, y, 'or')
ax.plot(xi, yi, '-b')
plt.show()