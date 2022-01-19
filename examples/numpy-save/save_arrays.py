"""
Example of saving several NumPy arrays into a single file and loading those
arrays from the saved file.
"""

import numpy as np

# Save arrays `a`, `b`, `c` to an `.npz` file

a = np.array([[4, 5, 81], [10, 2, 7], [1, 21, 5]])
b = np.array([[90, 51, 81], [10, 21, 74], [19, 1, 15]])
c = np.array([[0.1, 5.8, 0.71], [3.9, 2, 7.9], [1.05, 21, 5]])

with open('zdata.npz', 'wb') as file:
    np.savez(file, a=a, b=b, c=c)

# Load arrays `aa`, `bb`, `cc` from the `.npz` file

with np.load('zdata.npz') as data:
    aa = data['a']
    bb = data['b']
    cc = data['c']

# Print results

print('a is\n', a)
print('b is\n', b)
print('c is\n', c)

print('aa is\n', aa)
print('bb is\n', bb)
print('cc is\n', cc)
