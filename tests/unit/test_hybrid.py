"""
This is a module for testing the hybrid.py module
"""

import pytest
import numpy as np
from root_finding.hybrid import hybrid


def test_bisection_fail():

    def f(x):
        return x**2

    def df(x):
        return 2 * x

    roots = hybrid(f, df, -3, 3, tol1=1e-6, tol2=1e-12, max_iter1=1000, max_iter2=1000)
    roots = sorted(roots)

    assert len(roots) == 1
    assert np.allclose(roots, [0], atol=1e-10)


def test_correct_roots_2():

    def f(x):
        return x**2 - 4

    def df(x):
        return 2 * x

    roots = hybrid(f, df, -3, 3, tol1=1e-6, tol2=1e-12)
    roots = sorted(roots)

    assert len(roots) == 2
    assert np.allclose(roots, [-2.0, 2.0], atol=1e-10)


def test_correct_roots_3():

    def f(x):
        return x**3 - x

    def df(x):
        return 3 * x**2 - 1

    roots = hybrid(f, df, -2, 2, tol1=1e-6, tol2=1e-12)
    roots = sorted(roots)

    assert len(roots) == 3
    assert np.allclose(roots, [-1.0, 0.0, 1.0], atol=1e-10)
