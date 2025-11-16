# python_testing_project

## Getting Started

This project uses [uv](https://docs.astral.sh/uv/getting-started/installation/) for packaging and dependency management.

To install everything, run:

```zsh
uv sync
```

## Commands

| command | purpose |
| ------- | ------- |
| `uv sync` | install dependencies in environment |
| `uv run fastapi dev src/python_testing_project/main.py` | run development server on port :8000 |
| `uv run pytest -vv` | run [pytest](https://docs.pytest.org/en/stable/) verbosely |
| `uv run black .` | run [black](https://black.readthedocs.io/en/stable/index.html) code formatter |
| `uv run pytest -cov` | run [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) for test coverage report |
| `uv run coverage report` | generate test [coverage](https://coverage.readthedocs.io/en/7.11.3/) report |
| `uv run flake8` | run [flake8 for linting](https://flake8.pycqa.org/en/latest/index.html) |
