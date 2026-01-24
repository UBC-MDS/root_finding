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

    The interval ``[xmin, xmax]`` is split into ``N-1`` subintervals, and each
    subinterval is checked for a sign change indicating a root.

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
        The method converges when ``|xmax - xmin| < tol``.
        Default is ``1e-6``.
    max_iter : int, optional
        Maximum number of iterations allowed.
        Default is ``100``.
    N : int, optional
        Number of subintervals.
        Default is ``100`` (99 intervals).

    Returns
    -------
    roots : numpy.ndarray
        Estimated roots of the function ``f``.

    Raises
    ------
    RuntimeError
        If the algorithm fails to converge within ``max_iter`` iterations.
    TypeError
        If the inputs are not of the expected types.
    ValueError
        If ``xmax <= xmin``.

    Notes
    -----
    The bisection method requires that a root be enclosed within an interval
    ``[a, b]`` such that ``f(a) * f(b) < 0``.

    Convergence is achieved when:

    :math:`|x_{\max} - x_{\min}| < \mathrm{tol}`

    When searching for multiple roots, this method:

    * Is **not guaranteed** to find all roots
    * Cannot detect roots with multiplicity greater than one (e.g. ``x**2``)
    * May return duplicate roots

    Examples
    --------
    Find two simple roots:

    >>> roots = bisection_find_roots(lambda x: x**2 - 4, -3, 3, N=100)
    >>> roots
    array([-2.,  2.])

    Bisection may fail with large intervals:

    >>> roots = bisection_find_roots(lambda x: x**2 - 0.0001, -3, 3,
    ...                              tol=1e-9, max_iter=1000, N=100)
    >>> roots
    array([])

    Smaller intervals recover the roots:

    >>> roots = bisection_find_roots(lambda x: x**2 - 0.0001, -3, 3,
    ...                              tol=1e-9, max_iter=1000, N=1000)
    >>> roots
    array([-0.01,  0.01])

    Duplicate roots may be returned:

    >>> roots = bisection_find_roots(lambda x: x**2 - 1, -3, 3,
    ...                              tol=1e-9, N=100)
    >>> roots
    array([-1., -1.,  1.,  1.])
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
