import cv2 as cv
import numpy as np
import csv
from os import path

def image_setup(src):
    img_result = np.clip(src, 0, 255)
    img_result = img_result.astype('uint8')

    bw_img = cv.cvtColor(img_result, cv.COLOR_BGR2GRAY)
    _, bw_img = cv.threshold(bw_img, 254, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

    return bw_img

def find_centre(src):
    bin_img = image_setup(src)

    dist_map = cv.distanceTransform(bin_img, cv.DIST_L2, 3)
    
    mask = dist_map.copy()

    cv.normalize(mask, mask, 0, 1.0, cv.NORM_MINMAX)
    _, mask = cv.threshold(mask, 0, 1, cv.THRESH_BINARY)
    mask = mask.astype('uint8')
    mask *= 255
    
    mask = cv.ximgproc.thinning(mask, mask, cv.ximgproc.THINNING_GUOHALL)
        
    widths = cv.bitwise_and(dist_map, dist_map, mask=mask)
    
    mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
    mask[np.where((mask == [255,255,255]).all(axis=2))] = [0,0,255]
    
    return mask, widths


# #old function that messed up the spline generation because the points were not in 
# #adjecent order (i.e. adjacent points weren't next to each other in the csv)
# def extract_points(array: np.array):
#     result = []
#     x_coords, y_coords = np.nonzero(array)

#     for i in range(len(x_coords)):
#         x, y = x_coords[i], y_coords[i]
#         result.append((x,y,array[x,y],array[x,y]))

#     return result

def extract_points(img:np.ndarray):
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


def main(track):
    cwd = 'src/centreline_gen/'

    src = cv.imread(path.join(cwd,'tracks/', track+'_map.png'))
    
    result_img = src
    if src is None:
        print('ERROR: Image not found')
        exit(0)
    
    centreline, widths = find_centre(src)
    
    result = extract_points(widths)
    
    centre_mask = cv.inRange(centreline, (0,0,255), (0,0,255))

    # Replace the corresponding pixels in image1 with those from image2
    result_img[centre_mask > 0] = centreline[centre_mask > 0]

    cv.imwrite(path.join(cwd, 'output', track + '_centre.png'), result_img)
    cv.imwrite(path.join(cwd,'/output', track + '_widths.png'), widths)

    with open(path.join(cwd, 'output',track,'_centreline.csv'), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(result)
    

if __name__ == "__main__":
    track = 'Hockenheim'
    main(track)
