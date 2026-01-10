# Welcome to root_finding

## Contributors
Harrison Li, Devon Vorster, Li Pu

|        |        |
|--------|--------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/root_finding.svg)](https://pypi.org/project/root_finding/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/root_finding.svg)](https://pypi.org/project/root_finding/)  |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

*TODO: the above badges that indicate python version and package version will only work if your package is on PyPI.
If you don't plan to publish to PyPI, you can remove them.*

root_finding is a Python package designed to compare two classical numerical root-finding algorithms: the Bisection Method and the Newton–Raphson Method. The package provides a unified interface for solving one-dimensional nonlinear equations and emphasizes interpretability by exposing iteration histories, convergence behavior, and failure cases. Its primary goal is educational, allowing users to understand the strengths, limitations, and practical differences between these two methods through direct comparison.
.
## Package functionality

The root_finding package provides a small set of one-dimensional root-finding tools designed to compare classical numerical methods and visualize their behavior.

- `bisection`  
  Implements the Bisection Method for finding a root of a continuous one-dimensional function over a specified interval. This method is robust and guaranteed to converge under a sign-change condition, making it suitable as a baseline for comparison.

- `newton1d`  
  Implements the Newton–Raphson Method for one-dimensional root finding using an initial guess and derivative information. This method typically converges rapidly near the root but is sensitive to the choice of initial value and may fail when derivative conditions are unfavorable.

- `hybrid`  
  A hybrid root-finding approach that combines the robustness of the Bisection Method with the fast local convergence of the Newton–Raphson Method. This method aims to improve reliability while maintaining efficient convergence.

- `plot_root`  
  Provides a visualization of the target function and its roots, allowing users to inspect convergence behavior and compare methods graphically.

## Relation to the Python ecosystem

Root-finding algorithms are well established within the Python scientific computing ecosystem. Libraries such as SciPy provide highly optimized and general-purpose root solvers through modules like `scipy.optimize`, which include implementations of bisection-based methods, Newton-type methods, and hybrid algorithms.

In contrast, the `root_finding` package focuses on transparency and comparison rather than performance or generality. It is designed for learning and experimentation, with explicit access to iteration histories and convergence diagnostics, making it particularly suitable for educational settings and algorithmic analysis rather than production-level numerical computation.

Related packages include:
- SciPy root-finding tools: https://docs.scipy.org/doc/scipy/reference/optimize.html  
- `scipy.optimize.newton`: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.newton.html

## Get started

You can install this package into your preferred Python environment using pip:

```bash
$ pip install root_finding
```

TODO: Add a brief example of how to use the package to this section

To use root_finding in your code:

```python
>>> import root_finding
>>> root_finding.hello_world()
```

## Copyright

- Copyright © 2026 Harrison Li, Devon Vorster, Li Pu.
- Free software distributed under the [MIT License](./LICENSE).
