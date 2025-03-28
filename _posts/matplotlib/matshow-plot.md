---
title: Matshow Plot with Matplotlib
date: May 10, 2023
---

Visualize an array using Matplotlib's matshow function. The first example shown below plots a 2D array and the second example plots a diagonal array.

```python
import matplotlib.pyplot as plt
import numpy as np

a = np.random.rand(20, 20)

fig, ax = plt.subplots()
im = ax.matshow(a)
fig.colorbar(im, ax=ax)

plt.show()
```

<p><img src="../images/matplotlib-matshow-1.png" style="max-width:80%;" alt="matshow plot"></p>

```python
import matplotlib.pyplot as plt
import numpy as np

b = np.diag(range(15))

_, ax = plt.subplots()
ax.matshow(b, cmap='binary')

plt.show()
```

<p><img src="../images/matplotlib-matshow-2.png" style="max-width:80%;" alt="matshow plot"></p>
