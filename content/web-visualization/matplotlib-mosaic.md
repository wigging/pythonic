+++
title = "Mosaic grid of plots"
date = 2022-11-06
+++

Example of using Matplotlib `subplot_mosaic()` to create a grid of plots.

```python
import matplotlib.pyplot as plt

_, ax = plt.subplot_mosaic([['one', 'two'],
                            ['three', 'three']])

ax['one'].plot([3, 5, 6, 2, 8], '-o', color='red')

ax['two'].plot([7, 8, 4, 9], color='blue')

ax['three'].plot([1, 3, 4, 2, 3, 4], color='black')

plt.show()
```

<p><img src="/pythonic/img/matplotlib-mosaic.png" style="max-width:500px;" alt="mosaic plot"></p>
