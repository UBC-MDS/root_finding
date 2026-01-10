"""
A module that implements a root finding algorithm using Bisection
"""

from typing import Callable


def bisection(f: Callable[[float], float], xmin: float, xmax: float,
              tol1: float):
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
       tol1 : float
           Relative convergence tolerance for the bisection method.

       Returns
       -------
       x : float
           Estimated roots of the function `f`.

       Notes
       -----

       The bisection method requires that the root to be enclosed by the
       initial interval ``[xmin, xmax]``, i.e., ``f(xmin) * f(xmax) < 0``.
       It is used to produce an estimate that lies sufficiently close to
       the root when the relative convergence criteria ``tol1`` is satisfied:

       Where ``| (xmax - xmin) / xmid | < tol1``, ``xmid = (xmax + xmin) / 2``
    `
       Examples
       --------
       >>> bisection(f, 0, 2, 1e-12)
    """

    pass
