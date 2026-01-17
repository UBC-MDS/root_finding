"""
A module that provides visualization tools for root finding algorithms.
"""

from typing import Callable, Tuple
from root_finding.hybrid import hybrid
import numpy as np
import matplotlib.pyplot as plt


def plot_root(
    f: Callable[[float], float],
    dfdx: Callable[[float], float],
    xmin: float,
    xmax: float,
    tol1: float,
    tol2: float,
    max_iter1: int = 500,
    max_iter2: int = 500,
    npts: int = 1000,
    n: int = 50,
) -> Tuple[plt.Figure, plt.Axes]:
    r"""
    Plot a scalar function and visualize its roots using a hybrid
    bisection-Newton root-finding algorithm.

    This function computes the roots of a scalar function `f` within a
    given interval using the `hybrid` method and returns a Matplotlib
    figure containing the function plot and the detected roots.

    Parameters
    ----------
    f : callable
        Scalar function to be plotted. Must accept a single scalar argument.
    dfdx : callable
        Derivative of `f`. Must accept a single scalar argument.
    xmin : float
        Lower bound of the plotting and root-search interval.
    xmax : float
        Upper bound of the plotting and root-search interval.
    tol1 : float
        Convergence tolerance passed to the bisection-based root search
        stage of the hybrid method. Must be strictly positive.
    tol2 : float
        Relative convergence tolerance passed to the Newton-Raphson
        refinement stage of the hybrid method. Must be strictly positive.
    max_iter1 : int, optional
        Maximum number of iterations allowed for the bisection-based
        root search. Default is 500.
    max_iter2 : int, optional
        Maximum number of iterations allowed for Newton's method.
        Default is 500.
    npts : int, optional
        Number of points used to discretize the interval ``[xmin, xmax]``
        for plotting the function. Default is 1000.
    n : int, optional
        Number of subintervals used by the bisection-based root search.
        Passed to the hybrid solver. Default is 50.

    Returns
    -------
    fig : matplotlib.figure.Figure
        The Matplotlib figure object.
    ax : matplotlib.axes.Axes
        The Matplotlib axes containing the plot.

    Examples
    --------
    >>> f = lambda x: x**2 - 4
    >>> df = lambda x: 2*x
    >>> fig, ax = plot_root(f, df, -3, 3, 1e-6, 1e-12)
    >>> fig.savefig("roots.png")
    """

    # Compute roots
    roots = hybrid(f, dfdx, xmin, xmax, tol1, tol2, max_iter1, max_iter2, n)

    # Prepare data
    x = np.linspace(xmin, xmax, npts)
    f_vec = np.vectorize(f)

    # Create plot
    fig, ax = plt.subplots()
    ax.plot(x, f_vec(x), label="f(x)")
    ax.axhline(0, color="black", linewidth=0.8)

    for r in roots:
        ax.scatter(r, f_vec(r), label=f"x = {r}")

    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title("Root finding via Hybrid Bisection-Newton")
    ax.legend()
    ax.set_ylim(-1, 1)

    return fig, ax
