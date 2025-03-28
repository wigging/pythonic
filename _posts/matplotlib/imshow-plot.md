---
title: Imshow Plot with Matplotlib
date: May 10, 2023
---

Display data as an image using Matplotlib's imshow method.

```python
import matplotlib.pyplot as plt
import numpy as np

a = np.random.rand(100, 100)

_, ax = plt.subplots(tight_layout=True)
ax.imshow(a, interpolation='bilinear')

plt.show()
```

<p><img src="../images/matplotlib-imshow.png" style="max-width:80%;" alt="imshow plot"></p>
