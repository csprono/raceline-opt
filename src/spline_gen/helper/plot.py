import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

def plot_lines(line_properties:tuple, ax:plt.Axes, line_len:int, x_vals:np.ndarray):
    slopes, y_ints = line_properties

    pt_scalars = range(-line_len//2, line_len//2)
    
    find_line_ys = lambda x,slope,intercept: (slope * x) + intercept 

    line_xs = [x+pt_scalars for x in [x for x in x_vals]]

    line_points = []
    for slope,y_int,x in zip(slopes, y_ints, line_xs):
        line_points.append(np.column_stack((x,find_line_ys(x, slope, y_int))))

    line_points = np.array(line_points)
  
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
        
    to_plot = LineCollection(line_points, colors=colors, linestyle='solid', linewidth=0.5)
    ax.add_collection(to_plot)