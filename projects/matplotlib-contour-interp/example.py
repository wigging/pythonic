"""
Example of smoothing a contour plot by using zoom and gaussian functions from
SciPy. This example is based on the Stack Overflow post available at the
following URL https://stackoverflow.com/q/12274529/1084875
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter, zoom

# Get the data
# ----------------------------------------------------------------------------

data = np.loadtxt('data.txt')

# Example 1 - Create a contour plot of the original data
# ----------------------------------------------------------------------------

_, (ax1, ax2) = plt.subplots(ncols=2, tight_layout=True, figsize=[10, 4.8])
ax1.contour(data)
ax2.contourf(data)

# Example 2 - Resample data with zoom then create contour plot
# ----------------------------------------------------------------------------

data2 = zoom(data, 3)

_, (ax1, ax2) = plt.subplots(ncols=2, tight_layout=True, figsize=[10, 4.8])
ax1.contour(data2)
ax2.contourf(data2)

# Example 3 - Resample data with gaussian filter then create contour plot
# ----------------------------------------------------------------------------

data3 = gaussian_filter(data, 0.7)

_, (ax1, ax2) = plt.subplots(ncols=2, tight_layout=True, figsize=[10, 4.8])
ax1.contour(data3)
ax2.contourf(data3)

# Show plots
# ----------------------------------------------------------------------------

plt.show()
