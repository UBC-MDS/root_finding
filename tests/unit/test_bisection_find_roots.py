"""
This is a module for testing the bisection_find_roots.py module

The bisection method is a numerical method for finding the root of a function.
The root of a function is where it crosses the x-axis (for single valued functions),
and finding roots is analogous to solving equations. Not all equations are solvable
by hand, and in these cases we must refer to numerical approximations. The
bisection_find_roots method implements the bisection method over discrete intervals
in a given range in an attempt to find multiple roots for a given function.
"""

from root_finding.bisection.bisection_find_roots import bisection_find_roots
from typing import Sequence
import pytest
import numpy as np


# Define function fixtures


def func(x):
    """
    A function to test the correct root value are returned
    """
    return 3 * x**3 + 4 * x**2 - 2 * x - 2


def func_for_repeated_roots(x):
    """A function used to check multiple values for the same roots
    are not returned.
    """
    return x**2 - 1


def func_for_boundary_roots(x):
    """
    A function to test for roots at boundaries
    """
    return x**2 - 4


def func_no_roots(x):
    """
    A function that has no roots.
    """
    return x**2 + 10


# Tests


class TestBisectionFindRootsAccuracy:

    def test_finds_all_roots(self):
        """Test the function returns the correct outputs (roots)"""

        roots = bisection_find_roots(func, xmin=-2, xmax=2, tol=1e-9, max_iter=500)
        actual = np.array([func(root) for root in roots])
        expected = np.zeros(len(roots))

        assert isinstance(roots, Sequence)
        assert all(isinstance(x, float) for x in roots)
        assert np.allclose(actual, expected)

    def test_handles_boundary_roots(self):
        """Check function captures boundary roots"""
        roots_boundary = bisection_find_roots(
            func_for_boundary_roots, -2, 2, tol=1e-9, N=100
        )
        expected = np.array([-2.0, 2.0])

        # Check correct length i.e. no duplicated and captures boundaries
        assert len(roots_boundary) == 2  # actual == expected
        # Check roots are the expected values
        assert np.allclose(roots_boundary, expected)

    def test_handles_duplicate_roots(self):
        """Check function does not return duplicate values for roots in basic cases."""
        roots_repeated = bisection_find_roots(
            func_for_repeated_roots, -3, 3, tol=1e-9, N=100
        )
        expected = np.array([-1.0, 1.0])

        assert len(roots_repeated) == 2  # actual == expected
        # Check for correct returned roots
        assert np.allclose(roots_repeated, expected)

    def test_no_roots_found(self):
        """Check it returns an empty array when no roots exist."""
        roots = bisection_find_roots(
            func_no_roots, -10, 10, tol=1e-9, max_iter=100, N=100
        )
        assert isinstance(roots, Sequence)
        assert len(roots) == 0


class TestBisectionFindRootsErrors:

    @pytest.mark.parametrize(
        "f, xmin, xmax, tol, max_iter, N",
        [
            ("not_a_func", 0, 1, 1e-9, 200, 100),  # Bad f
            (func, "0", 1, 1e-9, 200, 100),  # Bad xmin
            (func, 1, "2", 1e-9, 200, 100),  # Bad xmax
            (func, 0, 1, "1e-9", 200, 100),  # Bad tol
            (func, 0, 1, 1e-9, 200.5, 100),  # Bad max_iter (float)
            (func, 0, 1, 1e-9, 200, 100.5),  # N is a float
        ],
    )
    def test_bad_input(self, f, xmin, xmax, tol, max_iter, N):
        """Test error handlinf for incorrect arguments types"""
        with pytest.raises(TypeError):
            bisection_find_roots(f, xmin, xmax, tol=tol, max_iter=max_iter, N=N)

    def test_convergence_failure(self):
        """Test convergence failure with impossible tolerance"""
        with pytest.raises(RuntimeError, match="Failed to converge in 200 iterations."):
            bisection_find_roots(func, xmin=-2, xmax=2, tol=1e-200, max_iter=200, N=100)

    def test_invalid_range(self):
        """Test case where xmin is greater than xmax"""
        with pytest.raises(ValueError):
            bisection_find_roots(func, xmin=2, xmax=1, tol=1e-9, max_iter=200)
