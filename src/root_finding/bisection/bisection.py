"""
A module that implements a root finding algorithm using Bisection
"""

from typing import Callable
import numpy as np


def bisection(
    f: Callable[[float], float],
    xmin: float,
    xmax: float,
    tol: float = 1e-9,
    max_iter=500,
) -> float:
    r"""
    Find a root of a scalar function using the bisection method.

    Parameters
    ----------
    f : callable
        Function whose root is sought. Must accept a single scalar argument.
    xmin : float
        Lower bound of the initial interval.
    xmax : float
        Upper bound of the initial interval.
    tol : float, optional
        Absolute convergence tolerance.
        Convergence is achieved when ``|xmax - xmin| < tol``.
        Default is ``1e-9``.
    max_iter : int, optional
        Maximum number of iterations allowed.
        Default is ``500``.

    Returns
    -------
    root : float
        Estimated root of the function ``f``.

    Raises
    ------
    ValueError
        If the initial interval ``[xmin, xmax]`` does not bracket a root
        (that is, if ``f(xmin)`` and ``f(xmax)`` have the same sign).
    RuntimeError
        If the algorithm fails to converge within ``max_iter`` iterations.
    TypeError
        If the inputs are not of the expected types.

    Notes
    -----
    The bisection method requires the root to be enclosed within the
    initial interval ``[xmin, xmax]`` such that:

    :math:`f(x_{\min}) \cdot f(x_{\max}) < 0`

    Convergence is guaranteed for continuous functions when this
    condition is satisfied and:

    :math:`|x_{\max} - x_{\min}| < \mathrm{tol}`

    Examples
    --------
    >>> root = bisection(lambda x: 3*x**3 + 4*x**2 - 2*x - 2, 0, 2, max_iter=500)
    >>> f"{root:.5f}"
    '0.74827'
    """

    # Error handling for correct inputs

    # note: correct type of f is enforced by python, raises TypeError

    if not (isinstance(xmin, (int, float))):
        raise TypeError("'xmin' should be a number.")

    if not (isinstance(xmax, (int, float))):
        raise TypeError("'xmax' should be a number.")

    if not isinstance(tol, float):
        raise TypeError("'tol' should be of type 'float'.")

    if not isinstance(max_iter, int):
        raise TypeError("'max_iter' should be of type 'int'.")

    if xmax <= xmin:
        raise ValueError("xmax should be greater than xmin")

    if np.sign(f(xmin)) == np.sign(f(xmax)):
        raise ValueError(
            "Incorrect boundary values, fxmax x fxmin needs to be less than 0."
        )

    # Bisection Method
    fmin = f(xmin)
    xmid = xmid = xmin + (xmax - xmin) / 2
    it = 0

    while (xmax - xmin) > tol:

        # Exit loop if we are at max iterations
        if it == max_iter:
            raise RuntimeError(f"Failed to converge in {max_iter} iterations.")

        # calculate xmid
        xmid = (xmax + xmin) / 2
        fmid = f(xmid)

        # Check if xmid is a root
        if fmid == 0:
            break

        # Test if root is in lower interval
        elif np.sign(fmin) != np.sign(fmid):
            # if yes use lower interval
            xmax = xmid

        else:
            # is no use upper interval
            xmin = xmid
            fmin = fmid
        it += 1

    # Return root approximation
    return xmid
