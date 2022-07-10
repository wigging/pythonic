"""
Create a Matplotlib animation using the FuncAnimation class.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(tight_layout=True)
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.1, 1.1)
line, = ax.plot([], [], '-ro', alpha=0.5)

xs = np.linspace(0, 2*np.pi, 128)
x = []
y = []


def update(i):
    x.append(i)
    y.append(np.sin(i))
    line.set_data(x, y)
    return line,


ani = FuncAnimation(fig, update, frames=xs, interval=20, repeat=False, blit=True)

# Uncomment to save animation, requires the ffmpeg framework
# ani.save('funcanim.mp4', fps=30)

# Uncomment to display animated figure
plt.show()
