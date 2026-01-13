"""
A module that implements a root finding algorithm using Bisection
"""

from typing import Callable


def bisection(
    f: Callable[[float], float],
    xmin: float,
    xmax: float,
    tol: float = 1e-6,
    max_iter=100,
) -> float:
    r"""
       Find roots of a scalar function using Bisection.

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

       Returns
       -------
       root : float
           The estimated root of the function `f`.

        Raises
        ------
        ValueError
            If the initial interval [xmin, xmax] does not bracket the root
            (i.e., if f(xmin) and f(xmax) have the same sign).
        RuntimeError
            If the algorithm fails to converge within `max_iter` iterations.

       Notes
       -----

       The bisection method requires that the root to be enclosed by the
       initial interval ``[xmin, xmax]``, i.e., ``f(xmin) * f(xmax) < 0``.
       It is used to produce an estimate that lies sufficiently close to
       the root when the relative convergence criteria ``tol`` is satisfied:

       Where ``| (xmax - xmin) | < tol``
    `
       Examples
        --------
        >>> root = bisection(lambda x: 3*x**3 + 4*x**2 - 2*x - 2, 0, 2, max_iter = 500)
        >>> print(f"{root:.5f}")
            0.74827
    """

    pass
