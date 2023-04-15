import math
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

track = np.loadtxt(r'src\centreline_gen\output\centre_line.csv',delimiter=',')

# sorted_indices = np.argsort(track[:, 0])
# track = track[sorted_indices]



def create_splines(centreline:np.ndarray):
    centreline = np.vstack([centreline, centreline[0]])
    
    x = centreline[::,0]
    y = centreline[::,1]
    
    tck,u = interpolate.splprep([x,y], s=300, per=True)
    xi, yi = interpolate.splev(np.linspace(0,1, len(x)), tck)
    
    # plot the result
    fig, ax = plt.subplots(1, 1)
    ax.plot(x, y, 'or')
    ax.plot(xi, yi, '-b')
    plt.show()


create_splines(track)