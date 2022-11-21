"""
Create a Matplotlib animation using the ArtistAnimation class.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

fig, ax = plt.subplots(tight_layout=True)
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.1, 1.1)

xs = np.linspace(0, 2*np.pi, 128)
x = []
y = []
ims = []

for i in range(len(xs)):
    x.append(xs[i])
    y.append(np.sin(xs[i]))
    im, = ax.plot(x, y, '-ro', alpha=0.5)
    ims.append([im])

ani = ArtistAnimation(fig, ims, interval=40, repeat=False)

# Uncomment to save animation, requires the ffmpeg framework
# ani.save('artistanim.mp4', fps=30)

# Uncomment to display animated figure
plt.show()
