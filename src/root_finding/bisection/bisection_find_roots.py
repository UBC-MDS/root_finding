"""
A module to search for roots by implementing a given root finding method.
"""

from root_finding.bisection.bisection import bisection
from typing import Callable, Sequence
import numpy as np


def bisection_find_roots(
    f: Callable[[float], float],
    xmin: float,
    xmax: float,
    tol: float = 1e-6,
    max_iter: int = 100,
    N: int = 100,
) -> Sequence[float]:
    r"""
       Find multiple roots of a scalar function using the bisection method.

       Split [xmin,xmax] into N-1 intervals and check for roots in each interval.

       Parameters
       ----------
       f : callable
           Function whose root is sought. Must accept a single scalar argument.
       xmin : float
           Lower bound of the initial interval.
       xmax : float
           Upper bound of the initial interval.
       tol : float, optional
           Absolute convergence tolerance for the bisection method.
           The method converges when |xmax - xmin| < `tol`.
           The default value is 1e-6.
        max_iter : int, optional
            maximum number of iterations allowable.
            Default is 100.
        N : int, optional
            Use to set number of intervals.
            Default is 100 (99 intervals).


       Returns
       -------
       roots : numpy array of floats
           The estimated roots of the function `f`.

        Raises
        ------
        RuntimeError
            If the algorithm fails to converge within `max_iter` iterations.
        TypeError
            If the inputs are not of the expected types.

       Notes
       -----

       The bisection method requires that the root to be enclosed by the
       initial interval ``[xmin, xmax]``, i.e., ``f(xmin) * f(xmax) < 0``.
       It is used to produce an estimate that lies sufficiently close to
       the root when the relative convergence criteria ``tol`` is satisfied:

       Where ``| (xmax - xmin) | < tol``

       In general when searching for multiple root value the bisection method
       is NOT guaranteed to find roots, and is NOT guaranteed to find roots
       with multiplicity greater than 1 (e.g. roots of x**2)

       This function may return duplicate roots.
    `
       Examples
        --------
        >>> roots = bisection_find_roots(lambda x: x**2 - 4, -3, 3, N=100)
        >>> print(roots)
            [-2.  2.]

        # Bisection method cannot find roots
        >>> roots = bisection_find_roots(lambda x: x**2 - 0.0001, -3, 3, tol=1e-9, max_iter = 1000, N=100)
        >>> print(roots)
            []

        # Smaller intervals now find roots
        >>> roots = bisection_find_roots(lambda x: x**2 - 0.0001, -3, 3, tol=1e-9, max_iter = 1000, N=1000)
        >>> print(roots)
            [-0.01  0.01]

        # Returns duplicate roots
        >>> roots = bisection_find_roots(lambda x: x**2 - 1, -3, 3, tol=1e-9, N=100)
        >>> print(roots)
            [-1. -1.  1.  1.]

    """

    # Input handling

    # f type input handled by python - returns TypeError

    if not (isinstance(xmin, (int, float))):
        raise TypeError("'xmin' should be of type 'float'.")

    if not (isinstance(xmax, (float, int))):
        raise TypeError("'xmax' should be of type 'float'.")

    if not isinstance(tol, float):
        raise TypeError("'tol' should be of type 'float'.")

    if not isinstance(max_iter, int):
        raise TypeError("'max_iter' should be of type 'int'.")

    if not isinstance(N, int):
        raise TypeError("'N' should be of type 'int'.")

    if xmax <= xmin:
        raise ValueError("xmax should be greater than xmin")

    # Initialize output
    roots = []

    # Create intervals
    x = np.linspace(xmin, xmax, N)
    try:
        y = f(x)
    except Exception:
        y = np.array([f(x) for x in x])

    # Check if xmin is a root
    if y[0] == 0:
        roots.append(x[0])

    for i in range(1, len(x)):
        # Check if interval boundary is a root
        if y[i] == 0:
            # Duplicate root protection
            if not roots or abs(x[i] - roots[-1]) > tol:
                # add boundary root to roots
                roots.append(x[i])

        # Check interval contains a root
        elif np.sign(y[i - 1]) != np.sign(y[i]):

            # Apply bisection method
            root = bisection(f, x[i - 1], x[i], tol, max_iter)

            # Duplicate root detection
            if not roots or abs(root - roots[-1]) > tol:
                # add root to roots
                roots.append(root)

    return roots
