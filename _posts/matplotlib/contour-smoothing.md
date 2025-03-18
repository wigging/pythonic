---
title: Contour plot smoothing with Matplotlib
date: February 4, 2023
---

The example below generates a contour plot of sparse data.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter, zoom

# Get the data
data = np.loadtxt('data.txt')

# Create a contour plot of the original data
_, (ax1, ax2) = plt.subplots(ncols=2, tight_layout=True, figsize=[10, 4.8])
ax1.contour(data)
ax2.contourf(data)
```

<p><img src="../../assets/images/matplotlib-contour-orig.pdf" style="max-width:100%;" alt="original"></p>

The plot can be smoothed by using SciPy's zoom function or gaussian filter function. Input parameters for each function should be adjusted accordingly for the data.

```python
# Resample the data with zoom then create contour plot
data2 = zoom(data, 3)

_, (ax1, ax2) = plt.subplots(ncols=2, tight_layout=True, figsize=[10, 4.8])
ax1.contour(data2)
ax2.contourf(data2)
```

<p><img src="../../assets/images/matplotlib-contour-zoom.pdf" style="max-width:100%;" alt="zoom"></p>

```python
# Resample data with gaussian filter then create contour plot
data3 = gaussian_filter(data, 0.7)

_, (ax1, ax2) = plt.subplots(ncols=2, tight_layout=True, figsize=[10, 4.8])
ax1.contour(data3)
ax2.contourf(data3)
```

<p><img src="../../assets/images/matplotlib-contour-gauss.pdf" style="max-width:100%;" alt="gaussian"></p>

The contour plot examples in this article are based on a Stack Overflow [post](https://stackoverflow.com/q/12274529/1084875) which is where the original data was obtained from.
