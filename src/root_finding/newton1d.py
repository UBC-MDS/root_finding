"""
A module that implements a root finding algorithm using Newton-Raphson method
"""

from typing import Callable


def newton1d(
    f: Callable[[float], float], df: Callable[[float], float], x0: float,
    tol1: float
):
    r"""
    Find roots of a scalar function using Newton-Raphson.

    Parameters
    ----------
    f : callable
        Function whose root is sought. Must accept a single scalar argument.
    df : callable
        Derivative of `f`. Must accept a single scalar argument.
    x0 : float
        Initial guess for the root.
    tol1 : float
        Relative convergence tolerance for the Newton-Raphson method.

    Returns
    -------
    x : float
        Estimated root of the function `f`.

    Notes
    -----
    The Newton-Raphson method updates the current estimate using the local
    linear approximation of `f` at the current point:

    ``x_{n+1} = x_n - f(x_n) / df(x_n)``.

    The iteration stops when the relative change in successive iterates is
    below the specified tolerance `tol1`, i.e., when:

    ``| (x_{n+1} - x_n) / x_{n+1} | < tol1``.

    This method often converges rapidly when `x0` is sufficiently close to the
    true root and `df(x)` is well-behaved, but it may fail when `df(x_n) = 0`
    or when the iterates diverge.

    Examples
    --------
    >>> f = lambda x: x**2 - 2
    >>> df = lambda x: 2*x
    >>> newton1d(f, df, 1.0, 1e-12)
    """
    pass
