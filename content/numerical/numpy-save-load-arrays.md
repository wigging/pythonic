+++
title = "Save and load arrays"
date = 2022-11-07
+++

NumPy arrays can be saved and loaded using different file formats. Examples of using the NumPy file formats `.npy` and `.npz` as well as a plain text format are given below.

## Using the npy format

Use the NumPy `save()` function to save an array to a `.npy` file. Use the `load()` function to load the array from the file.

```python
import numpy as np

# Save an array named `z` to an `.npy` file

z = np.array([[3, 4, 8.91], [1.05, 2, 7], [5.4, 3, 1]])

with open('zarray.npy', 'wb') as file:
    np.save(file, z)

# Load the array data from the `.npy` file into `zz`

with open('zarray.npy', 'rb') as file:
    zz = np.load(file)

# Print results

print('z is\n', z)
print('zz is\n', zz)
```

Output from the above example is shown below.

```
z is
 [[3.   4.   8.91]
  [1.05 2.   7.  ]
  [5.4  3.   1.  ]]

zz is
 [[3.   4.   8.91]
  [1.05 2.   7.  ]
  [5.4  3.   1.  ]]
```

## Using the npz format

Use the `savez()` function to save several arrays to a single `.npz` file. Use the `load()` function to load the saved arrays from the file.

```python
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

```

Output from this example is given below.

```
a is
 [[ 4  5 81]
  [10  2  7]
  [ 1 21  5]]
b is
 [[90 51 81]
  [10 21 74]
  [19  1 15]]
c is
 [[ 0.1   5.8   0.71]
  [ 3.9   2.    7.9 ]
  [ 1.05 21.    5.  ]]

aa is
 [[ 4  5 81]
  [10  2  7]
  [ 1 21  5]]
bb is
 [[90 51 81]
  [10 21 74]
  [19  1 15]]
cc is
 [[ 0.1   5.8   0.71]
  [ 3.9   2.    7.9 ]
  [ 1.05 21.    5.  ]]
```

## Using plain text format

A plain text format can also be used to save and load a NumPy array with the `savetxt()` and `loadtxt()` functions.

```python
import numpy as np

# Save array to a text file

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

np.savetxt('array.txt', a)

# Load array from a text file named `array.txt`

b = np.loadtxt('array.txt')

# Print comparison of `a` and `b`

print('a is\n', a)
print('b is\n', b)
```
