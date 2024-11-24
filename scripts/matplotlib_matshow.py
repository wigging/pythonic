"""
Visualize an array using Matplotlib's matshow function.
"""

import matplotlib.pyplot as plt
import numpy as np

# Example 1
# ----------------------------------------------------------------------------

a = np.random.rand(20, 20)

fig, ax = plt.subplots()
im = ax.matshow(a)
fig.colorbar(im, ax=ax)

# Example 2
# ----------------------------------------------------------------------------

b = np.diag(range(15))

_, ax = plt.subplots()
ax.matshow(b, cmap='binary')

plt.show()
