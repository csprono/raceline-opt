import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from math import atan, pi

def create_splines(centreline:np.ndarray):
    centreline = np.vstack([centreline, centreline[0]])
    
    x = centreline[::,0]
    y = centreline[::,1]
    
    spline_tck, u = interpolate.splprep([x,y], s=175) 
    
    #evaluate spline at given point
    xi, yi = interpolate.splev(u, spline_tck)
    
    # # plot the result
    # fig, ax = plt.subplots(1, 1)
    # ax.plot(x, y, 'or')
    # ax.plot(xi, yi, '-b')
    # plt.show()

    return spline_tck, u

def get_slope(splinerep_tck:tuple, u):
    dx, dy = interpolate.splev(u, splinerep_tck, der=1)
    return dy/dx   

def calc_normals(splinerep_tck:tuple, u, x_vals, y_vals):
    norm_slopes = -1/get_slope(splinerep_tck, u) #array of slopes at each point 
    
    y_ints = y_vals - norm_slopes * x_vals #array of y_ints for tangents at each point
        
    return norm_slopes, y_ints

def calc_tangents(splinerep_tck:tuple, u, x_vals, y_vals):
    tan_slopes = get_slope(splinerep_tck, u) #array of slopes at each point 
       
    y_ints = y_vals - tan_slopes * x_vals #array of y_ints for tangents at each point
        
    return tan_slopes, y_ints

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

def find_curvature():
    pass

def main():
    centreline = np.loadtxt(r'src\centreline_gen\output\centre_line.csv', delimiter = ',')
    x = centreline[::,0]
    y = centreline[::,1]

    spline_tck, u = interpolate.splprep([x,y], s=175)
    spline_x, spline_y = interpolate.splev(u, spline_tck)

    dx_dt, dy_dt = interpolate.splev(u, spline_tck, der=1)
    ddx_dt, ddy_dt = interpolate.splev(u, spline_tck, der=2)
    

    magnitude = (dx_dt ** 2 + dy_dt ** 2) ** 0.5
    unit_tangent_vector = (dx_dt / magnitude, dy_dt / magnitude)

    numerator = abs(ddx_dt * unit_tangent_vector[1] - ddy_dt * unit_tangent_vector[0])
    denominator = (dx_dt ** 2 + dy_dt ** 2) ** (3 / 2)
    curvature = numerator / denominator

    fig, ax = plt.subplots()
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
  
    plt.plot([spline_x,spline_x+unit_tangent_vector[0]], [spline_y,spline_y+unit_tangent_vector[1]])
    plt.plot(spline_x,spline_y)
    plt.show()



if __name__ == '__main__':
    main()

 