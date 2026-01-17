"""
This is a module for testing the hybrid.py module
Parts of the tests are suggested and implemented by ChatGPT
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


def func(x):
    return 3 * x**3 + 4 * x**2 - 2 * x - 2


def dfdx(x):
    return 9 * x**2 + 8 * x - 2


@pytest.mark.parametrize(
    "func, dfdx, xmin, xmax, tol1, tol2, max_iter1, max_iter2, n",
    [
        ("not_a_func", dfdx, 0, 1, 1e-9, 1e-9, 200, 200, 50),  # Bad f
        (func, "not_a_func", 0, 1, 1e-9, 1e-9, 200, 200, 50),  # Bad dfdx
        (func, dfdx, "0", 1, 1e-9, 1e-9, 200, 200, 50),  # Bad xmin
        (func, dfdx, 0, "1", 1e-9, 1e-9, 200, 200, 50),  # Bad xmax
        (func, dfdx, 0, 1, "1e-9", 1e-9, 200, 200, 50),  # Bad tol1
        (func, dfdx, 0, 1, 1e-9, "1e-9", 200, 200, 50),  # Bad tol2
        (func, dfdx, 0, 1, 1e-9, 1e-9, "200", 200, 50),  # Bad max_iter1 
        (func, dfdx, 0, 1, 1e-9, 1e-9, 200.5, 200, 50),  # Bad max_iter1 
        (func, dfdx, 0, 1, 1e-9, 1e-9, 200, 200, "50"),  # Bad n
        (func, dfdx, 0, 1, 1e-9, 1e-9, 200, 200, 0.5),  # Bad n
    ],
)
def test_bad_input_type_errors(
    func, dfdx, xmin, xmax, tol1, tol2, max_iter1, max_iter2, n
):
    """Test cases where input is not the expected type."""
    with pytest.raises(TypeError):
        hybrid(func, dfdx, xmin, xmax, tol1, tol2, max_iter1, max_iter2, n)


@pytest.mark.parametrize(
    "func, dfdx, xmin, xmax, tol1, tol2, max_iter1, max_iter2, n",
    [
        (func, dfdx, 0, 1, 1e-9, 1e-9, 0, 200, 50),  # Bad max_iter1
        (func, dfdx, 0, 1, 1e-9, 1e-9, -100, 200, 50),  # Bad max_iter1
        (func, dfdx, 0, 1, 1e-9, 1e-9, 200, 200.5, 50),  # Bad max_iter2
        (func, dfdx, 0, 1, 1e-9, 1e-9, 200, 0, 50),  # Bad max_iter2
        (func, dfdx, 0, 1, 1e-9, 1e-9, 200, -100, 50),  # Bad max_iter2
        (func, dfdx, 0, 1, 1e-9, 1e-9, 200, 200, -50),  # Bad n
    ],
)
def test_bad_input_value_errors(
    func, dfdx, xmin, xmax, tol1, tol2, max_iter1, max_iter2, n
):
    """Test cases where input is not the expected type."""
    with pytest.raises(ValueError):
        hybrid(func, dfdx, xmin, xmax, tol1, tol2, max_iter1, max_iter2, n)


def test_xmax_less_than_xmin():
    with pytest.raises(ValueError):
        hybrid(
            f=lambda x: x - 1,
            dfdx=lambda x: 1,
            xmin=2,
            xmax=1,
            tol1=1e-6,
            tol2=1e-12,
        )


def test_output_is_finite_array():

    def f(x):
        return x**2 - 2

    def df(x):
        return 2 * x

    roots = hybrid(f, df, 0, 2, tol1=1e-6, tol2=1e-12)

    assert isinstance(roots, (list, np.ndarray))
    assert np.all(np.isfinite(roots))


def test_close_roots():

    def f(x):
        return (x - 1e-4) * (x + 1e-4)

    def df(x):
        return 2 * x

    roots = hybrid(f, df, -1, 1, tol1=1e-6, tol2=1e-10)
    roots = sorted(roots)

    assert np.allclose(roots, [-1e-4, 1e-4], atol=1e-8)


def test_transcendental_function():

    def f(x):
        return np.cos(x) - x

    def df(x):
        return -np.sin(x) - 1

    roots = hybrid(f, df, 0, 2, tol1=1e-3, tol2=1e-12)

    assert len(roots) == 1
    assert abs(roots[0] - 0.7390851332151607) < 1e-10


def test_duplicate_bisection_roots_collapsed():

    def f(x):
        return x**2 - 1

    def df(x):
        return 2 * x

    roots = hybrid(f, df, -3, 3, tol1=1e-6, tol2=1e-8)
    roots = sorted(roots)

    assert len(roots) == 2
    assert np.allclose(roots, [-1.0, 1.0], atol=1e-8)


def test_root_at_interval_boundary():

    def f(x):
        return x * (x - 2)

    def df(x):
        return 2 * x - 2

    roots = hybrid(f, df, 0, 3, tol1=1e-6, tol2=1e-12)
    roots = sorted(roots)

    assert np.allclose(roots, [0.0, 2.0], atol=1e-10)


def test_no_roots_in_interval():

    def f(x):
        return x**2 + 1

    def df(x):
        return 2 * x

    with pytest.raises(RuntimeError):
        hybrid(f, df, -3, 3, tol1=1e-6, tol2=1e-12)
