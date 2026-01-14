"""
This is a module for testing the bisection.py module
"""

# from typing import Sequence
# import numpy as np

from root_finding.bisection import bisection

import pytest
import math


def func(x):
    return 3 * x**3 + 4 * x**2 - 2 * x - 2


##########################################
#
# bisection for multiple roots -- not guaranteed

# def func_for_roots_at_boundaries(x):
#     # roots at -2, and +3
#     return (x+2)*(x-3)

# func = np.vectorize(func)
# func_for_roots_at_boundaries = np.vectorize(func_for_roots_at_boundaries)

##########################################

# check function is converging in expected number of steps
# check floating point errors are not mkaing us miss values. -round to tolerance


def test_bisection_output():

    # First root
    root1 = bisection(func, xmin=-2, xmax=-1, tol=1e-9, max_iter=200)

    # Second root
    root2 = bisection(func, xmin=-1, xmax=0, tol=1e-9, max_iter=200)

    # Third root
    root3 = bisection(func, xmin=0, xmax=1, tol=1e-9, max_iter=200)

    # Test outputs are floats.
    assert isinstance(root1, float)

    # Test roots are true roots
    assert math.isclose(func(root1), 0.0, abs_tol=1e-8)
    assert math.isclose(func(root2), 0.0, abs_tol=1e-8)
    assert math.isclose(func(root3), 0.0, abs_tol=1e-8)


def test_bisection_bad_input():

    # define non-callable object for incorrect function input
    fake_func = "fake_func"

    # check correct input types - typeErrors
    with pytest.raises(TypeError):
        bisection(func, xmin="2", xmax=1, tol=1e-9, max_iter=200)

    with pytest.raises(TypeError):
        bisection(func, xmin=2, xmax="1", tol=1e-9, max_iter=200)

    with pytest.raises(TypeError):
        bisection(func, xmin=0, xmax=2, tol="1e-9", max_iter=200)

    with pytest.raises(TypeError):
        bisection(func, xmin=0, xmax=2, tol=1e-9, max_iter=200.5)

    with pytest.raises(TypeError):
        bisection(fake_func, xmin=0, xmax=2, tol=1e-9, max_iter=200)


def test_bisection_runtime_error():
    # test funciton raises runtime errors
    pass


def test_bisection_value_error():
    # ensure a root exists via IVT
    pass


## Bisection for multiple roots is not guaranteed!
# def test_bisection_roots_at_boundary():
#     # test it finds roots at boundaries.
#     bisection(func_for_roots_at_boundaries, xmin=-2, xmax=2, tol=1e-6, max_iter=200)

#     pass
