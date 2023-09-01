---
title: Gauss-Legendre points and weights
date: August 31, 2023
---

The function below returns the Gauss-Legendre integration points and weights for a 2D quadrilateral using values from a 1D quadrature. The 1D values are obtained from NumPy's `leggauss()` function.

```python
def gauss2D(n):

    x, w = np.polynomial.legendre.leggauss(n)

    weights = []
    gauss_pts = []

    for i in range(n):
        for j in range(n):
            wts = w[i] * w[j]
            weights.append(wts)

            g = [x[i], x[j]]
            gauss_pts.append(g)

    return np.array(weights), np.array(gauss_pts)
```

Here is an example of using the function for `n = 2` sample points. The printed output is also shown below.

```python
n = 2
w, g = gauss2D(n)
print('weights\n', w)
print('gauss points\n', g)
```

```text
weights
 [1. 1. 1. 1.]
gauss points
 [[-0.57735027 -0.57735027]
 [-0.57735027  0.57735027]
 [ 0.57735027 -0.57735027]
 [ 0.57735027  0.57735027]]
```

The for-loops can be removed by using some NumPy tricks as shown below. This returns the same results as the previous function.

```python
def gauss2Dnumpy(n):

    x, w = np.polynomial.legendre.leggauss(n)

    mesh = np.meshgrid(x, x, indexing='ij')
    gauss_pts = np.array(mesh).reshape(2, -1).T

    weights = (w * w[:, None]).ravel()

    return weights, gauss_pts
```
