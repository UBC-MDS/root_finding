"""
A module that implements a root finding algorithm using Newton-Raphson method.
"""

from __future__ import annotations

from typing import Callable, Sequence
import math
import numpy as np


def newton1d(
    f: Callable[[float], float],
    df: Callable[[float], float],
    x0: float,
    tol1: float,
    max_iter: int = 100,
    eps_df: float = 1e-14,
) -> Sequence[float]:
    r"""
    Find roots of a scalar function using Newton–Raphson.

    Parameters
    ----------
    f : callable
        Function whose root is sought. Must accept a single scalar argument.
    df : callable
        Derivative of `f`. Must accept a single scalar argument.
    x0 : float or Sequence[float]
        Initial guesses for the root.
    tol1 : float
        Relative convergence tolerance for the Newton–Raphson method.
        Must be strictly positive.
    max_iter : int, default=100
        Maximum number of iterations before declaring non-convergence.
    eps_df : float, default=1e-14
        Threshold to treat the derivative as "too close to zero" to avoid
        division by ~0.

    Returns
    -------
    x_arr : Sequence[float]
        Estimated roots of the function `f`.

    Notes
    -----
    The Newton–Raphson method updates the current estimate using the local
    linear approximation of `f` at the current point:

    ``x_{n+1} = x_n - f(x_n) / df(x_n)``.

    Convergence is declared when the step size is sufficiently small in a
    relative sense:

    ``|x_{n+1} - x_n| <= tol1 * max(1, |x_{n+1}|)``.

    This is numerically safer than ``|(x_{n+1}-x_n)/x_{n+1}|`` because it avoids
    division by zero when ``x_{n+1} = 0``.

    The method often converges rapidly when `x0` is sufficiently close to the
    true root and `df(x)` is well-behaved, but it may fail when `df(x_n) = 0`
    (or very close to zero) or when the iterates diverge.

    Raises
    ------
    TypeError
        If `f` or `df` is not callable.
    ValueError
        If `tol1 <= 0`, `max_iter <= 0`, `x0` is not finite, or `df(x)` is too
        close to zero during iteration.
    RuntimeError
        If the method does not converge within `max_iter` iterations.

    Examples
    --------
    >>> f = lambda x: x**2 - 2
    >>> df = lambda x: 2*x
    >>> root = newton1d(f, df, 1.0, 1e-12)
    >>> abs(root - 2**0.5) < 1e-10
    True
    """
    # Defensive input checks (rubric: exception handling)
    if not callable(f) or not callable(df):
        raise TypeError("f and df must be callable.")
    if tol1 <= 0:
        raise ValueError("tol1 must be > 0.")
    if not isinstance(max_iter, int) or max_iter <= 0:
        raise ValueError("max_iter must be a positive integer.")
    if type(x0) is float or type(x0) is int:
        x0 = [x0]
    for x in x0:
        if not math.isfinite(x):
            raise ValueError("All x0 must be a finite number.")

    x_arr = np.array([])

    for x in x0:
        x_old = float(x)

        for k in range(1, max_iter + 1):
            fx = float(f(x_old))
            dfx = float(df(x_old))

            if not math.isfinite(fx) or not math.isfinite(dfx):
                raise ValueError("f(x) and df(x) must be finite during iteration.")

            if abs(dfx) < eps_df:
                raise ValueError(
                    f"Derivative too close to zero at iter={k}, x={x_old} (df={dfx})."
                )

            x_new = x_old - fx / dfx

            if not math.isfinite(x_new):
                raise ValueError(f"Non-finite iterate encountered at iter={k}.")

            # Convergence check (safe relative criterion)
            if abs(x_new - x_old) <= tol1 * max(1.0, abs(x_new)):
                if all(x_new - x_arr > tol1 * max(1.0, abs(x_new))):
                    x_arr = np.append(x_arr, x_new)

            x_old = x_new

    if len(x_arr) == 0:
        raise RuntimeError(f"Newton method did not converge within {max_iter} iterations.")
    else:
        return x_arr

