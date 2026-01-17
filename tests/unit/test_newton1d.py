import math
import pytest

from root_finding.newton1d import newton1d


def test_newton1d_converges_quadratic_root2():
    # f(x)=x^2-2 has root sqrt(2)
    f = lambda x: x**2 - 2
    df = lambda x: 2 * x
    root = newton1d(f, df, x0=1.0, tol1=1e-12)
    assert abs(root - math.sqrt(2)) < 1e-10


def test_newton1d_initial_guess_is_root():
    # If x0 is already a root, method should return quickly and accurately
    f = lambda x: x - 3
    df = lambda x: 1.0
    root = newton1d(f, df, x0=3.0, tol1=1e-12)
    assert abs(root - 3.0) < 1e-12


def test_newton1d_when_derivative_too_small():
    # df(x)=0 at x=0 -> should be fine
    f = lambda x: x**3
    df = lambda x: 3 * x**2
    root = newton1d(f, df, x0=0.0, tol1=1e-12)
    assert abs(root - 0) < 1e-12


def test_newton1d_raises_when_tol_not_positive():
    f = lambda x: x - 1
    df = lambda x: 1.0
    with pytest.raises(ValueError):
        newton1d(f, df, x0=0.0, tol1=0.0)
    with pytest.raises(ValueError):
        newton1d(f, df, x0=0.0, tol1=-1e-6)


def test_newton1d_raises_on_nonconvergence_with_small_max_iter():
    # Intentionally make it fail by forcing very small max_iter
    f = lambda x: x**2 - 2
    df = lambda x: 2 * x
    with pytest.raises(RuntimeError):
        newton1d(f, df, x0=1.0, tol1=1e-30, max_iter=1)
