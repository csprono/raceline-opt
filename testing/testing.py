import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

def create_splines(centreline:np.ndarray):
    centreline = np.vstack([centreline, centreline[0]])
    
    x = centreline[::,0]
    y = centreline[::,1]
    
    tck, u = interpolate.splprep([x,y], s=300, per=True)
    
    #evaluate spline at given point
    xi, yi = interpolate.splev(np.linspace(0,1, len(x)), tck)
    
    # plot the result
    fig, ax = plt.subplots(1, 1)
    ax.plot(x, y, 'or')
    ax.plot(xi, yi, '-b')
    plt.show()

    return tck

def get_slope(splinerep_tck:tuple, point):
    slope = interpolate.splev(point, splinerep_tck, der=1)
    return slope   

def calc_tangent(splinerep_tck:tuple, point):
    tan_slope = get_slope(splinerep_tck, point)

    y_int = y - tan_slope * x
    
    tangent_y = lambda x: tan_slope * x + y_int

def calc_normal(splinerep_tck:tuple, point):
    norm_slope = -1/get_slope(splinerep_tck, point)

    y_int = y - norm_slope * x
    norm_y = lambda x: norm_slope * x + y_int

centreline = np.loadtxt(r'src\centreline_gen\output\centre_line.csv', delimiter = ',')
x = centreline[::,0]
y = centreline[::,1]

spline_tck = create_splines(centreline)

tangents = calc_tangent(spline_tck, np.linspace(0,1, len(x)))

#evaluate spline at given point
xi, yi = interpolate.splev(np.linspace(0,1, len(x)), tck)

# plot the result
fig, ax = plt.subplots(1, 1)
ax.plot(x, y, 'or')
ax.plot(xi, yi, '-b')
ax.plot(tangents)
plt.show()