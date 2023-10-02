import cv2 as cv
import numpy as np
from scipy.interpolate import splev, splprep
import matplotlib.pyplot as plt

def adjust_bodyfit(occ_grid : np.ndarray, width) -> np.ndarray:
    '''
        Inputs: 
        occ_grid = Occupancy grid with interpolated boundary
        resolution = distance per pixel

        Output:
        - shrunken_track = Occupancy grid that depicts drivable area and accounts 
          for width of the car
    '''
    
    shrinkage_amount = width # TODO need to account for resolution to check how many pixels to shrink by
    kernel_size = (shrinkage_amount // 2, shrinkage_amount // 2)
    kernel = np.ones(kernel_size, np.uint8)

    shrunken_track = cv.erode(occ_grid, kernel)
    
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
        if cv.contourArea(contours[i]) < 100:
            continue
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
    cv.imwrite('contours.png', new)

    #clean boundary arrays
    left = [inner.flatten() for inner in np.vstack(left)]
    right = [inner.flatten() for inner in np.vstack(right)]

    left, right = np.array(left), np.array(right)

    return left, right

def interpolate_bounds(occ_grid, left, right):
    x_l, y_l = left[::,0], left[::,1]
    x_r, y_r = right[::,0], right[::,1] 
    
    spline_tck_l, u_l = splprep([x_l, y_l], s=2, per=True) # can tune s
    spline_tck_r, u_r = splprep([x_r, y_r], s=2, per=True) # can tune s

    #evaluate spline at given point
    xi_l, yi_l = splev(np.linspace(0,1,1000), spline_tck_l)
    xi_r, yi_r = splev(np.linspace(0,1,1000), spline_tck_r)

    interp_left, interp_right = np.column_stack((xi_l, yi_l)), np.column_stack((xi_r, yi_r))

    for pt in np.vstack((interp_left, interp_right)):
        occ_grid[round(pt[1])][round(pt[0])] = 255

    
    # # for debugging
    # cv.imshow('interpolated', occ_grid)
    # # plot the result
    # fig, ax = plt.subplots(1, 1)
    # ax.plot(x_l, y_l, 'or')
    # ax.plot(xi_l, yi_l, '-r')
    # ax.plot(x_r, y_r, 'ob')
    # ax.plot(xi_r, yi_r, '-b')

    # plt.show()


    return 


src = cv.imread('testcase.png', cv.IMREAD_GRAYSCALE)
cv.imshow('init', src)

left_arr = np.loadtxt('testcase_L.csv', delimiter=',')
right_arr = np.loadtxt('testcase_R.csv', delimiter=',')

x_list = np.arange(0, 100, 1)
y_list = np.arange(0, 100, 1)


interpolate_bounds(src, left_arr, right_arr)
cv.imshow('interp', src)


# bodyfit prep (interpolation needs to be included)
filled = src.copy()
start = (50,19) # probably just use first entry in conemap or something
cv.floodFill(filled, None, start, 255)
cv.imshow('filled', filled)
cv.imwrite('filled.png', filled)

shrunken_track = adjust_bodyfit(filled, 2)
cv.imshow('shrunken', shrunken_track)

left, right = separate_l_r(shrunken_track)


print(left)
print(right)
cv.imshow('init', src)
cv.imshow('edges', edges_only)

cv.waitKey(0)