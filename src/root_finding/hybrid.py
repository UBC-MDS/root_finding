"""
A module that implements a root finding algorithm using Bisection and
Newton-Raphson method combined.
"""

from typing import Callable, Sequence
from root_finding.newton1d import newton1d
from root_finding.bisection.bisection_find_roots import bisection_find_roots


def hybrid(
    f: Callable[[float], float],
    dfdx: Callable[[float], float],
    xmin: float,
    xmax: float,
    tol1: float,
    tol2: float,
    max_iter1=500, 
    max_iter2=500
) -> Sequence[float]:
    r"""
    Find multiple roots of a scalar function using a hybrid
    Bisection-Newton method.

    This algorithm combines a robust bisection-based root searching
    stage with Newton-Raphson refinement to efficiently locate all
    detectable roots within a given interval.

    Parameters
    ----------
    f : callable
        Function whose roots are sought. Must accept a single scalar argument.
    dfdx : callable
        Derivative of `f`. Must accept a single scalar argument.
    xmin : float
        Lower bound of the search interval.
    xmax : float
        Upper bound of the search interval.
    tol1 : float
        Absolute or relative convergence tolerance used by the bisection-based
        root search. This tolerance controls the accuracy of the initial
        guesses passed to Newton's method and must be strictly positive.
    tol2 : float
        Relative convergence tolerance used by the Newton-Raphson method.
        Must be strictly positive.
    max_iter1 : int
        Maximum number of iteration for bisection method, Default = 500
    max_iter2 : int
        Maximum number of iteration for Newton's method, Default = 500

    Returns
    -------
    roots : Sequence[float]
        A sequence of estimated roots of the function `f` within the
        interval ``[xmin, xmax]``.  
        Only roots for which Newton's method converges successfully are
        returned. The output may be empty if no convergent roots are found.

    Notes
    -----
    The hybrid algorithm proceeds in two stages:

    1. **Bisection-based root search**  
       The interval ``[xmin, xmax]`` is subdivided and examined for sign
       changes of `f`. Each detected sign change (or exact zero) produces
       an initial root estimate using the bisection method via
       `bisection_find_roots`.

       This stage is robust but may:
       - Miss roots of even multiplicity
       - Miss roots if the subdivision is too coarse
       - Return duplicate or closely spaced root estimates

    2. **Newton-Raphson refinement**  
       Each bisection-derived estimate is passed as an initial guess to
       `newton1d`, which rapidly refines the root when the derivative
       is well-behaved.

       Newton's method may fail to converge if:
       - The derivative is zero or nearly zero
       - The initial guess is too far from a true root
       - The iterates diverge or become non-finite

    Duplicate roots produced by either stage may be filtered using the
    Newton convergence tolerance ``tol2``.

    Convergence for Newton's method is declared when:

    ``|x_{n+1} - x_n| <= tol2 * max(1, |x_{n+1}|)``.

    This hybrid approach improves robustness compared to Newton's method
    alone while achieving faster convergence than pure bisection.

    See Also
    --------
    bisection_find_roots :
        Bisection-based root search for detecting multiple candidate roots.
    newton1d :
        Newton-Raphson method for fast local root refinement.

    Examples
    --------
    >>> f = lambda x: x**2 - 4
    >>> df = lambda x: 2*x
    >>> roots = hybrid(f, df, -3, 3, tol1=1e-6, tol2=1e-12)
    >>> sorted(roots)
    [-2.0, 2.0]

    >>> f = lambda x: x**3 - x
    >>> df = lambda x: 3*x**2 - 1
    >>> roots = hybrid(f, df, -2, 2, tol1=1e-6, tol2=1e-12)
    >>> sorted(roots)
    [-1.0, 0.0, 1.0]
    """

    x_b = bisection_find_roots(f, xmin, xmax, tol1, max_iter=max_iter1)

    roots = newton1d(f, dfdx, x_b, tol2, max_iter=max_iter2)

    return roots