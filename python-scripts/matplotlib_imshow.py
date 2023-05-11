"""
Display data as an image using Matplotlib's imshow method.
"""

import matplotlib.pyplot as plt
import numpy as np

a = np.random.rand(100, 100)

_, ax = plt.subplots(tight_layout=True)
ax.imshow(a, interpolation='bilinear')

plt.show()
