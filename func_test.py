import timeit
import numpy as np
import cv2 as cv    
import csv
from adt import Stack

import sys
sys.setrecursionlimit(100000)

sample = cv.imread('output/track_widths.png')
sample = cv.cvtColor(sample, cv.COLOR_BGR2GRAY)

visited = {}
track_widths = []
centreline_points = []

DIRECTIONS = [(0,1), (1,1), (1,0), (1,-1), (0,-1),(-1,-1), (-1,0), (-1,1)]
NON_EDGE = 0.0

starting_point = (56,380)

def dfs(point):
    if point not in visited:
        visited[point] = True
        track_widths.append(np.array([sample[point[1]][point[0]], sample[point[1]][point[0]]]))
        centreline_points.append(np.array(point))

        for dir in DIRECTIONS:
            if (sample[point[1] + dir[1]][point[0] + dir[0]] != NON_EDGE and (point[0] + dir[0], point[1] + dir[1]) not in visited):
                dfs((point[0] + dir[0], point[1] + dir[1]))
            
    return

print('test')

dfs(starting_point)

test_out = np.zeros(sample.shape)
i = 0
for x,y in centreline_points:
    test_out[y][x] = 255
    dist = track_widths[i]
    
    test_out[][]
    cv.imshow('test',test_out)
    cv.waitKey(10)
    i+=1


print(len(sample))
print(len(track_widths))