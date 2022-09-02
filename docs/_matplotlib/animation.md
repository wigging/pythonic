---
title: Animation
permalink: animation
---

Matplotlib provides two animation classes for animating a plot figure. The example below uses the ArtistAnimation class. The animation can be displayed just like any other Matplotlib figure and saved to file as various video formats.

```python
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

# Save animation to a movie file, requires the ffmpeg framework
ani.save('artistanim.mp4', fps=30)

plt.show()
```

This example creates a Matplotlib animation using the FuncAnimation class.

```python
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

# Save animation to a movie file, requires the ffmpeg framework
ani.save('funcanim.mp4', fps=30)

# Uncomment to display animated figure
plt.show()
```

Both examples generate the animated line plot shown below.

<video controls style="max-width:600px;">
    <source src="/pythonic/images/artistanim.mp4" type="video/mp4">
    Sorry, your browser doesn't support this embedded video.
</video>
