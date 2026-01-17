"""
This is a module for testing the bisection.py module
"""

# from typing import Sequence
# import numpy as np

from root_finding.bisection.bisection import bisection
import pytest


def func(x):
    return 3 * x**3 + 4 * x**2 - 2 * x - 2


# Use to test case when fmid == 0
def func_2(x):
    # y=0 at x=-1
    return 2 * x + 2


# --- Accuracy Tests ---
class TestBisectionAccuracy:

    @pytest.mark.parametrize(
        "xmin, xmax, expected",
        [
            (-2, -1, -1.479356),  # root 1
            (-1, 0, -0.602249),  # root 2
            (0, 1, 0.748272),  # root 3
        ],
    )
    def test_finds_correct_roots(self, xmin, xmax, expected):
        """Test for correct outputs."""
        root = bisection(func, xmin, xmax, tol=1e-9, max_iter=200)

        # Test the function returns the correct outputs
        assert root == pytest.approx(expected, abs=1e-6)
        assert func(root) == pytest.approx(0, abs=1e-6)

    def test_midpoint_is_root(self):
        """Test case when f(xmid) is exactly 0."""
        root = bisection(func_2, xmin=-2, xmax=0, tol=1e-9, max_iter=200)
        assert root == pytest.approx(-1.0, abs=1e-8)


# --- Error Hanlding Tests ---
class TestBisectionErrors:

    @pytest.mark.parametrize(
        "f, xmin, xmax, tol, max_iter",
        [
            ("not_a_func", 0, 1, 1e-9, 200),  # Bad f
            (func, "0", 1, 1e-9, 200),  # Bad xmin
            (func, 1, "2", 1e-9, 200),  # Bad xmax
            (func, 0, 1, "1e-9", 200),  # Bad tol
            (func, 0, 1, 1e-9, 200.5),  # Bad max_iter (float)
        ],
    )
    def test_type_errors(self, f, xmin, xmax, tol, max_iter):
        """Test cases where input is not the expected type."""
        with pytest.raises(TypeError):
            bisection(f, xmin, xmax, tol, max_iter)

    def test_convergence_failure(self):
        """Test convergence failure with impossible tolerance"""
        with pytest.raises(
            RuntimeError, match=f"Failed to converge in 100 iterations."
        ):
            bisection(func, 0, 2, tol=1e-200, max_iter=100)

    def test_invalid_range(self):
        """Test case where xmin is greater than xmax"""
        with pytest.raises(ValueError, match="xmax should be greater than xmin"):
            bisection(func, xmin=2, xmax=0, tol=1e-9, max_iter=100)

    def test_no_root(self):
        """Test case where f(xmin) and f(xmax) have same sign"""
        with pytest.raises(
            ValueError,
            match="Incorrect boundary values, fxmax x fxmin needs to be less than 0.",
        ):
            bisection(func, xmin=1, xmax=2, tol=1e-9, max_iter=100)
