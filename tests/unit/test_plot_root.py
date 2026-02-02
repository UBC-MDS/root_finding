"""
This is a module for testing the plot_root.py module.

The tests verify that the plotting utility correctly visualizes the
function, its roots (computed via the hybrid method), and returns
valid Matplotlib objects with appropriate labels and annotations. 
Parts of the tests and documentations are suggested and implemented 
by ChatGPT.
"""

import pytest
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PathCollection
from root_finding.plot_root import plot_root


def test_plot():
    """
    Test that plot_root returns valid Matplotlib Figure and Axes objects.

    This is a basic smoke test to ensure the plotting function executes
    without errors for a well-behaved function and returns the expected
    Matplotlib objects.
    """
    f = lambda x: x**3 - x
    df = lambda x: 3 * x**2 - 1
    xmin, xmax = -2, 2
    tol1, tol2 = 1e-6, 1e-12

    fig, ax = plot_root(f, df, xmin, xmax, tol1, tol2)
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)


def test_plot_root_basic():
    """
    Test that plot_root correctly visualizes a function with two real roots.

    The test checks:
    - The returned objects are Matplotlib Figure and Axes
    - The function curve is plotted and labeled
    - The correct number of root markers are displayed
    - Axis labels and title are properly set
    """
    # Simple quadratic function with two roots
    f = lambda x: x**2 - 4
    df = lambda x: 2 * x
    xmin, xmax = -3, 3
    tol1, tol2 = 1e-6, 1e-12

    fig, ax = plot_root(f, df, xmin, xmax, tol1, tol2)

    # Check that returned objects are Matplotlib figure and axes
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)

    # Check that function line exists
    lines = ax.get_lines()
    assert any("f(x)" in line.get_label() for line in lines)

    # Check that number of root markers matches expected roots
    roots = [-2.0, 2.0]
    scatter_points = [c for c in ax.collections if isinstance(c, PathCollection)]
    plotted_points = sum([len(c.get_offsets()) for c in scatter_points])
    assert plotted_points == len(roots)

    # Check labels and title
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "f(x)"
    assert "Hybrid" in ax.get_title()


def test_plot_root_single_root():
    """
    Test that plot_root correctly handles and displays a single root.

    The quadratic f(x) = x^2 has one real root at x = 0. The test verifies
    that exactly one root marker is plotted.
    """
    # Quadratic with a single root at zero
    f = lambda x: x**2
    df = lambda x: 2 * x
    xmin, xmax = -1, 1
    tol1, tol2 = 1e-6, 1e-12

    fig, ax = plot_root(f, df, xmin, xmax, tol1, tol2)

    scatter_points = [c for c in ax.collections if isinstance(c, PathCollection)]
    plotted_points = sum([len(c.get_offsets()) for c in scatter_points])
    assert plotted_points == 1  # only root at 0
