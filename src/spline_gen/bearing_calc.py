import numpy as np
from math import atan, pi

# #v1
# def calc_bearing(line_properties:tuple, spline_x):
#     slopes, y_ints = line_properties
#     x_vals = spline_x

#     find_line_ys = lambda x,slope,intercept: (slope * x) + intercept

#     line_points = []
#     north_points = []
#     origins = []
#     for slope,y_int,x in zip(slopes, y_ints, x_vals):
#         origin_y = find_line_ys(x, slope, y_int)
#         line_y = find_line_ys(x+1, slope, y_int)
        
#         line_points.append((x+1,line_y))
#         north_points.append((x, line_y))
#         origins.append((x, origin_y))

#     origins = np.array(origins)
#     line_points = np.array(line_points)
#     north_points = np.array(north_points)
    
#     opposite = ((north_points[::,0] - line_points[::,0])**2 + (north_points[::,1] - line_points[::,1])**2)**0.5
#     adjacent = ((north_points[::,0] - origins[::,0])**2 + (north_points[::,1] - origins[::,1])**2)**0.5

#     bearing = np.arctan(opposite/adjacent)
#     return bearing

def calc_bearing(line_properties:tuple):
    slopes, y_ints = line_properties
    
    bearings = []
    for slope in slopes:
        if slope > 0:
            bearings.append(atan(slope))
        elif slope == 0:
            bearings.append(0.5*pi)
        elif slope < 0:
            bearings.append(pi - atan(abs(slope)))
        else:
            bearings.append(0)

    bearings = np.array(bearings)
    
    return bearings