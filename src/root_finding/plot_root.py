"""
A module that provides visualization tools for root finding algorithms.
"""

# import numpy as np
# import matplotlib.pyplot as plt
from typing import Callable, Sequence


def plot_root(
    f: Callable[[float], float],
    roots: Sequence[float],
    xmin: float,
    xmax: float,
    npts: int = 1000,
):
    r"""
    Plot a scalar function and mark its roots.

    Parameters
    ----------
    f : callable
        Scalar function to be plotted. Must accept a single float argument.
    roots : sequence of float
        Roots of the function to be highlighted on the plot.
    xmin : float
        Lower bound of the plotting interval.
    xmax : float
        Upper bound of the plotting interval.
    npts : int, optional
        Number of points used to discretize the interval ``[xmin, xmax]``.
        Default is 1000.

    Returns
    -------
    None

    See Also
    --------
    bisection : Bisection method
    newton1d : Newton-Raphson method (1 dimensional)
    hybrid : Combines Bisection and Newton-Raphson

    Notes
    -----
    The function ``f(x)`` is plotted over the interval ``[xmin, xmax]``.
    The x-axis is also shown to help visualize where the roots occur.
    Each root will be marked with a red dot.

    Examples
    --------
    >>> roots = hybrid(f, dfdx, 0, 2, 1e-12, 1e-12)
    >>> plot_roots(f, roots, 0, 2)
    """
    pass
