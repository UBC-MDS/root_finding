"""
A module that implements a root finding algorithm using Bisection
"""

from typing import Callable, Sequence


def bisection(
    f: Callable[[float], float],
    xmin: float,
    xmax: float,
    tol: float = 1e-6,
    max_iter=100,
) -> Sequence[float]:
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
    # Error handling for correct inputs

    # note: correc type of f is enforced by python, raises TypeError

    if not (isinstance(xmin, float) or isinstance(xmax, int)):
        raise TypeError("'xmin' should be of type 'float'.")

    if not (isinstance(xmax, float) or isinstance(xmax, int)):
        raise TypeError("'xmax' should be of type 'float'.")

    if not isinstance(tol, float):
        raise TypeError("'tol' should be of type 'float'.")

    if not isinstance(max_iter, int):
        raise TypeError("'max_iter' should be of type 'int'.")

    if xmax <= xmin:
        raise ValueError("xmax should be greater than xmin")

    if f(xmin) * f(xmax) > 0:
        raise ValueError(
            "Incorrect boundary values, f(xmax)*f(xmin) needs to be less than 0."
        )

    xmid = 0
    it = 0
    while abs(xmax - xmin) > tol:

        # Exit loop if we are at max iterations
        if it == max_iter:
            raise RuntimeError(
                f"Convergence failed, total iterations reached: {max_iter}"
            )
        # calculate xmid
        xmid = (xmax + xmin) / 2

        # Check if xmid is a root
        if f(xmid) == 0:
            break

        # Test if root is in lower interval
        if f(xmin) * f(xmid) < 0:
            # if yes use lower interval
            xmax = xmid
            it += 1
        else:
            # is no use upper interval
            xmin = xmid
            it += 1

    # Return root approximation
    return xmid
