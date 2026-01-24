# Welcome to root_finding

## Contributors
Harrison Li, Devon Vorster, Li Pu

root_finding is a Python package designed to compare two classical numerical root-finding algorithms: the Bisection Method and the Newton–Raphson Method. The package provides a unified interface for solving one-dimensional nonlinear equations and emphasizes interpretability by exposing iteration histories, convergence behavior, and failure cases. Its primary goal is educational, allowing users to understand the strengths, limitations, and practical differences between these two methods through direct comparison.

## Documentation

Full documentation is available at: https://github.com/Harrisonlee0530/root_finding

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

## Installation

### For Users

You can install this package into your preferred Python environment using pip:

```bash
pip install root_finding
```

*(Note: Package is currently under development and not yet published to PyPI)*

### For Developers

To contribute to the development of this package:

1. **Clone the repository**
   ```bash
   git clone git@github.com:Harrisonlee0530/root_finding.git
   cd root_finding
   ```

2. **Set up the development environment**
   
   We use conda/mamba for environment management. Create the environment from the provided `environment.yml` file:
   
   ```bash
   conda env create -f environment.yml
   conda activate root_finding
   ```
   
   Or if you use mamba (faster):
   
   ```bash
   mamba env create -f environment.yml
   mamba activate root_finding
   ```

3. **Install the package in development mode**
   ```bash
   pip install -e .
   ```

## Get started

To use root_finding in your code:

```python
import root_finding
from root_finding.bisection.bisection import bisection
from root_finding.newton1d import newton1d

# Define a function: x^2 - 4
def f(x):
    return x**2 - 4

# Find root using bisection
root_bisection = bisection(f, xmin=0, xmax=3, tol=1e-6)
print(f"Bisection root: {root_bisection}")

# Find root using Newton-Raphson
def df(x):
    return 2*x

roots_newton = newton1d(f, df, x0=1.0, tol1=1e-6)
print(f"Newton root: {roots_newton[0]}")
```

For more examples, see the [Tutorial](https://harrisonlee0530.github.io/root_finding/tutorial.html) in our documentation.

## Running Tests

We use pytest for testing. To run the test suite:

```bash
# Run all tests
pytest

# Run tests with coverage report
pytest --cov=root_finding --cov-report=term-missing --cov-report=xml

# Run tests in parallel (faster)
pytest -n auto
```

## Building Documentation

Our documentation is built using Quarto and quartodoc and automatically deployed to GitHub Pages.

### Prerequisites

1. **Install Quarto**
   
   Download and install Quarto from https://quarto.org/docs/get-started/
   
   Or using conda:
   ```bash
   conda install -c conda-forge quarto
   ```

2. **Install quartodoc**
   ```bash
   pip install quartodoc
   ```

### Build the Documentation Locally

```bash
# Navigate to the documentation directory
cd qdocs

# Build the API reference
quartodoc build

# Preview the documentation locally
quarto preview

# Build the static site (optional)
quarto render
```

The documentation will be generated in the `qdocs/_site/` directory.

### Automatic Deployment

Documentation is automatically built and deployed to GitHub Pages when changes are pushed to the `main` branch. The deployment is handled by a GitHub Actions workflow defined in `.github/workflows/deploy.yml`.

The deployed documentation is available at: https://harrisonlee0530.github.io/root_finding/

## Project Structure

```
root_finding/
├── src/root_finding/          # Source code
│   ├── bisection/            # Bisection method implementation
│   │   ├── __init__.py
│   │   ├── bisection.py
│   │   └── bisection_find_roots.py
│   ├── newton1d.py           # Newton-Raphson implementation
│   ├── hybrid.py             # Hybrid method implementation
│   └── plot_root.py          # Visualization tools
├── tests/                    # Test suite
├── qdocs/                    # Documentation source
│   ├── _quarto.yml          # Quarto configuration
│   ├── index.qmd            # Home page
│   ├── tutorial.qmd         # Tutorial
│   └── reference/           # Generated API reference
├── .github/workflows/        # GitHub Actions workflows
│   └── deploy.yml           # Documentation deployment
├── pyproject.toml           # Project configuration
├── environment.yml          # Conda environment specification
└── README.md               # This file
```

## Development Workflow

1. **Create a new branch** for your feature
   ```bash
   git checkout -b feature-name
   ```

2. **Make your changes** and add tests

3. **Run tests** to ensure everything works
   ```bash
   pytest
   ```

4. **Update documentation** if needed
   ```bash
   cd qdocs
   quartodoc build
   quarto preview
   ```

5. **Commit and push** your changes
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin feature-name
   ```

6. **Create a pull request** on GitHub

## Copyright

- Copyright © 2026 Harrison Li, Devon Vorster, Li Pu.
- Free software distributed under the [MIT License](./LICENSE).
