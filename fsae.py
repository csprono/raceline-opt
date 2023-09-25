import cv2 as cv
import numpy as np

def adjust_bodyfit(occ_grid : np.ndarray) -> np.ndarray:
    '''
        Inputs: 
        occ_grid = Occupancy grid with interpolated boundary
        resolution = distance per pixel

        Output:
        - shrunken_track = Occupancy grid that depicts drivable area and accounts 
          for width of the car
    '''
    
    shrinkage_amount = 15 #need to account for resolution to check how many pixels to shrink by
    kernel_size = (shrinkage_amount // 2, shrinkage_amount // 2)
    kernel = np.ones(kernel_size, np.uint8)

    shrunken_track = cv.erode(filled, kernel)
    
    return shrunken_track


def separate_l_r(occ_grid : np.ndarray):
    '''
        Inputs:
        occ_grid = Eroded occupancy grid 

        Output:
        - left = list of arrays containing points of left boundary
        - right = list of arrays containing points of right boundary
    '''
    #separate inside from outside
    contours, hierarchy = cv.findContours(occ_grid, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)

    new = cv.cvtColor(occ_grid, cv.COLOR_GRAY2BGR)

    left, right = [],[]

    for i in range(len(contours)):
        # Draw the contour
        if hierarchy[0][i][3] == -1:
            # Outer contour, draw in red
            cv.drawContours(new, contours, i, (0, 0, 255), 1)

            # Outer contour, store its points
            right.append(contours[i])
        else:
            # Inner contour, draw in blue
            cv.drawContours(new, contours, i, (255, 0, 0), 1)

            # Inner contour, store its points
            left.append(contours[i])

    cv.imshow('contours', new)
    
    #clean boundary arrays
    left = [inner.flatten() for inner in np.vstack(left)]
    right = [inner.flatten() for inner in np.vstack(right)]

    left, right = np.array(left), np.array(right)

    return left, right

src = cv.imread('track.png')

edges_only = cv.Canny(src, threshold1=30, threshold2=100)

filled = edges_only.copy()

# bodyfit prep (interpolation needs to be included)
start = (941,385) # probably just user first entry in conemap or something
cv.floodFill(filled, None, start, 255)

shrunken_track = adjust_bodyfit(filled)

left, right = separate_l_r(shrunken_track)


print(left)
print(right)
cv.imshow('init', src)
# cv.imshow('edges', edges_only)
# cv.imshow('filled', filled)
# cv.imshow('shrunken', shrunken_track)

cv.waitKey(0)

