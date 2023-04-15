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
