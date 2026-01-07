"""
A module that implements a root finding algorithm using Bisection and
Newton-Raphson method combined.
"""


from typing import Callable


def hybrid(f: Callable[[float], float], dfdx: Callable[[float], float], 
           xmin: float, xmax: float, tol1: float, tol2: float):
    r"""
    Find roots of a scalar function using Bisection and Newton Raphson method.

    The algorithm first applies the bisection method to obtain a robust
    initial estimate of the root, then refines this estimate using
    Newton's method.

    Parameters
    ----------
    f : callable
        Function whose root is sought. Must accept a single scalar argument.
    dfdx : callable
        Function for the derivative of `f`. Must accept a single scalar
        argument.
    xmin : float
        Lower bound of the initial interval.
    xmax : float
        Upper bound of the initial interval.
    tol1 : float
        Relative convergence tolerance for the bisection method.
    tol2 : float
        Relative convergence tolerance for Newton's method.

    Returns
    -------
    x : float
        Estimated roots of the function `f`.

    See Also
    --------
    bisection : The Bisection Method
    newton1d : The Newton-Raphson Method


    Notes
    -----
    This hybrid approach combines the bisection method and Newton-Raphson
    method.

    The bisection method requires that the root to be enclosed by the
    initial interval ``[xmin, xmax]``, i.e., ``f(xmin) * f(xmax) < 0``.
    It is used to produce an estimate that lies sufficiently close to
    the root when the relative convergence criteria ``tol1`` is satisfied.

    Where ``| (xmax - xmin) / xmid | < tol1``, ``xmid = (xmax + xmin) / 2``

    The Newton-Raphson method is then applied using the output from the
    bisection method. 

    Where ``| (x_next - x_current) / x_next | < tol2``


    Examples
    --------
    >>> hybrid(f, dfdx, 0, 2, 1e-12, 1e-12)
    """

    pass