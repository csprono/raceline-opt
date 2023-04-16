import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection



def create_splines(centreline:np.ndarray):
    centreline = np.vstack([centreline, centreline[0]])
    
    x = centreline[::,0]
    y = centreline[::,1]
    
    spline_tck, u = interpolate.splprep([x,y], s=300) 
    
    #evaluate spline at given point
    xi, yi = interpolate.splev(u, spline_tck)
    
    return spline_tck, u

def get_slope(splinerep_tck:tuple, u):
    dx, dy = interpolate.splev(u, splinerep_tck, der=1)
    return dy/dx   

def calc_tangent(splinerep_tck:tuple, u, x_vals, y_vals):
    tan_slopes = get_slope(splinerep_tck, u) #array of slopes at each point 
       
    y_ints = y_vals - tan_slopes * x_vals #array of y_ints for tangents at each point
    find_tan_y = lambda x,slope,intercept: (slope * x) + intercept 
    
    tan_len = 4
    pt_scalars = range(-tan_len//2,tan_len//2+1)
    
    tan_xs = [x+pt_scalars for x in [x for x in x_vals]]
    tan_ys = []
    
    for slope,y_int,x in zip(tan_slopes, y_ints, tan_xs):
        tan_ys.append(np.column_stack((x,find_tan_y(x, slope, y_int))))

    tan_ys = np.array(tan_ys)
    
    return tan_ys

def main():
    centreline = np.loadtxt(r'src\centreline_gen\output\centre_line.csv', delimiter = ',')
    x = centreline[::,0]
    y = centreline[::,1]

    spline_tck, u = create_splines(centreline)
    spline_x, spline_y = interpolate.splev(u, spline_tck)

    tangents_y = calc_tangent(spline_tck, u, spline_x, spline_y)

    # plot the result
    fig, ax = plt.subplots(1, 1)
    ax.plot(x, y, 'or', label = 'data')
    ax.plot(spline_x, spline_y, '-k', label = 'spline',  linewidth=1.5)
    
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    to_plot = [[tangents_y[i]] for i in range(len(tangents_y))]
    
    tans = LineCollection(tangents_y, colors=colors, linestyle='solid', linewidth=0.5)
    ax.add_collection(tans)


    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()