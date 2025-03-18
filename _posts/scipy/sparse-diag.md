---
title: Sparse diagonal matrix with SciPy
date: November 8, 2022
---

The `diags` function from SciPy can be used to create a sparse diagonal matrix. The matrix is constructed from lists or NumPy arrays that represent the diagonals of the matrix. The `offsets` argument sets the placement of the diagonals within the matrix where `k = 0` is the main diagonal, `k < 0` is the kth lower diagonal, and `k > 0` is the kth upper diagonal.

```python
from scipy.sparse import diags

# Diagonals as lists or NumPy arrays
a = [33, 33, 33, 33]
b = [44, 44, 44, 44, 44]
c = [55, 55, 55, 55]

# Create a sparse diagonal matrix
z = diags([a, b, c], offsets=[1, 0, -1]).toarray()
```

Where `z` is a NumPy array containing the diagonals

```python
>>> z
array([[44, 33,  0,  0,  0],
       [55, 44, 33,  0,  0],
       [ 0, 55, 44, 33,  0],
       [ 0,  0, 55, 44, 33],
       [ 0,  0,  0, 55, 44]])
```
