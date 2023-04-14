import math
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

track = np.loadtxt(r'src\centreline_gen\output\centre_line.csv',delimiter=',')

# sorted_indices = np.argsort(track[:, 0])
# track = track[sorted_indices]


# track = np.vstack([track, track[0]])



x = track [:100:,0]
y = track[:100:,1]

tck,u = interpolate.splprep([x,y], s=0,)
xi, yi = interpolate.splev(np.linspace(0, 1, 1000), tck)

# plot the result
fig, ax = plt.subplots(1, 1)
ax.plot(x, y, 'or')
ax.plot(xi, yi, '-b')
plt.show()