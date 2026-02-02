# Welcome to root_finding

## Contributors
Harrison Li, Devon Vorster, Li Pu

root_finding is a Python package designed to compare two classical numerical root-finding algorithms: the Bisection Method and the Newton–Raphson Method. The package provides a unified interface for solving one-dimensional nonlinear equations and emphasizes interpretability by exposing iteration histories, convergence behavior, and failure cases. Its primary goal is educational, allowing users to understand the strengths, limitations, and practical differences between these two methods through direct comparison.

## Documentation

Full documentation is available at: https://harrisonlee0530.github.io/root_finding/

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

To install this package directly from GitHub:

```bash
pip install git+https://github.com/Harrisonlee0530/root_finding.git
```

*(Note: Package is currently under development and not yet published to PyPI. Once published, you will be able to install via `pip install root_finding`)*

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

4. **Install testing dependencies** (required for running tests)
   ```bash
   pip install pytest pytest-cov pytest-xdist
   ```

## Get started

To use root_finding in your code:

```python
from root_finding import bisection, newton1d

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

We use pytest for testing. Make sure you have installed the testing dependencies first (see step 4 in the installation instructions above).

To run the test suite:

```bash
# Run all tests
pytest

# Run tests with coverage report
pytest --cov=root_finding --cov-report=term-missing --cov-report=xml

# Run tests in parallel (faster, requires pytest-xdist)
pytest -n auto
```

## Building Documentation

Our documentation is built using Quarto and quartodoc.

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
cd docs

# Build the API reference
quartodoc build

# Preview the documentation locally
quarto preview

# Build the static site (optional)
quarto render
```

The documentation will be generated in the `docs/_site/` directory.

### Automatic Deployment

Documentation is automatically built and deployed to GitHub Pages when changes are pushed to the main branch. The deployment is handled by GitHub Actions workflows defined in `.github/workflows/deploy.yml` and `.github/workflows/docs.yml`.

The deployed documentation is available at: https://harrisonlee0530.github.io/root_finding/

## Project Structure

```
root_finding/
├── .github/                  # GitHub configuration
│   ├── ISSUE_TEMPLATE/      # Issue templates
│   │   ├── 01-bug-report.yml
│   │   └── config.yml
│   ├── workflows/           # GitHub Actions workflows
│   │   ├── deploy.yml       # Documentation deployment
│   │   ├── docs.yml         # Documentation build
│   │   └── pytest.yml       # Test automation
│   └── PULL_REQUEST_TEMPLATE.md
├── src/root_finding/        # Source code
│   ├── bisection/          # Bisection method implementation
│   │   ├── __init__.py
│   │   ├── bisection.py
│   │   └── bisection_find_roots.py
│   ├── __init__.py
│   ├── hybrid.py           # Hybrid method implementation
│   ├── newton1d.py         # Newton-Raphson implementation
│   └── plot_root.py        # Visualization tools
├── tests/                  # Test suite
│   ├── unit/              # Unit tests
│   │   ├── test_bisection.py
│   │   ├── test_bisection_find_roots.py
│   │   ├── test_example.py
│   │   ├── test_hybrid.py
│   │   ├── test_newton1d.py
│   │   └── test_plot_root.py
│   └── ...
├── docs/                   # Documentation source (Quarto)
│   ├── reference/         # API reference documentation
│   │   ├── bisection.bisection.qmd
│   │   ├── bisection.bisection_find_roots.qmd
│   │   ├── hybrid.qmd
│   │   ├── newton1d.qmd
│   │   ├── plot_root.qmd
│   │   └── ...
│   ├── index.qmd          # Home page
│   ├── reference.qmd      # API reference index
│   └── tutorial.qmd       # Tutorial
├── _quarto.yml            # Quarto configuration
├── pyproject.toml         # Project configuration
├── environment.yml        # Conda environment specification
├── CHANGELOG.md           # Version history
├── CODE_OF_CONDUCT.md     # Community guidelines
├── CONTRIBUTING.md        # Contribution guidelines
├── DEVELOPMENT.md         # Development documentation
├── LICENSE                # MIT License
└── README.md             # This file
```

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) and [Development Documentation](DEVELOPMENT.md) for details on how to contribute to this project.

Please also review our [Code of Conduct](CODE_OF_CONDUCT.md) before participating.

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
   cd docs
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