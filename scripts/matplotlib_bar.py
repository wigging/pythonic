"""
Example of a bar plot with value labels.
"""

import matplotlib.pyplot as plt

beers = ['bud lite', 'coors', 'yuengling', 'miller']
drinks = [20, 40, 80, 50]

_, ax = plt.subplots()
ax.bar(beers, drinks)
ax.bar_label(ax.containers[0], label_type='edge')
ax.set_xlabel('Beer')
ax.set_ylabel('Drinks')

plt.show()
