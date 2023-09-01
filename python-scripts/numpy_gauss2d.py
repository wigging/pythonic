import numpy as np


def gauss2D(n):
    """
    Get the Gauss-Legendre integration points and weights for a 2D
    quadrilateral using values from a 1D quadrature.
    """
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


def gauss2Dnumpy(n):
    """
    Get the Gauss-Legendre integration points and weights for a 2D
    quadrilateral using values from a 1D quadrature.

    Parameters
    ----------
    n : int
        Number of 1D integration points.

    Returns
    -------
    weights : ndarray
        Weights associated with the Gauss-Legendre integration points.
    gauss_pts : ndarray
        Gauss-Legendre points for a 2D quadrilateral master element.
    """
    x, w = np.polynomial.legendre.leggauss(n)

    mesh = np.meshgrid(x, x, indexing='ij')
    gauss_pts = np.array(mesh).reshape(2, -1).T

    weights = (w * w[:, None]).ravel()

    return weights, gauss_pts


if __name__ == '__main__':

    for n in range(2, 5):
        print('n =', n, '\n')

        w, g = gauss2D(n)
        print('weights\n', w)
        print('gauss pts\n', g, '\n')

        wnp, gnp = gauss2Dnumpy(n)
        print('weights (numpy)\n', w)
        print('gauss pts (numpy)\n', g, '\n')
