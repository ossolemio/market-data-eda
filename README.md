# market-data-eda

# I creataed the todo list of creating and setting up the initial repo:

Market Data EDA — Repository Bootstrap Guide
This guide documents the initial setup for the market-data-eda Python project. It follows a production-minded workflow for an AI Engineering learning project: version control first, an isolated environment, reproducible dependencies, code-quality tooling, and a clean project layout.

Project scope: This repository is for exploratory data analysis and data-quality practice with market data. It is educational and research-oriented only—not financial advice and not a source of trading signals.

1. Create the GitHub Repository
Sign in to GitHub.

Select New repository.

Set the repository name to market-data-eda.

Choose the appropriate visibility:

Public if it will be a portfolio project.

Private if the work is not ready to share.

Do not initialize the repository with a README, .gitignore, or license, because the project files will be created locally.

Create the repository.

Copy the repository’s HTTPS clone URL. It will look like this:

text
https://github.com/YOUR_GITHUB_USERNAME/market-data-eda.git
Replace YOUR_GITHUB_USERNAME with your actual GitHub username.

2. Clone It with VS Code
Open Visual Studio Code.

Press Ctrl+Shift+P on Windows/Linux, or Cmd+Shift+P on macOS.

Type and select Git: Clone.

Paste the GitHub repository clone URL.

Choose a local parent folder where your projects live.

When VS Code asks whether to open the cloned repository, choose Open.

Open the integrated terminal with Ctrl+` .

Confirm that the terminal is in the repository root:

bash
git status
You should see that you are on the default branch with no project files committed yet.

3. Create and Activate a Virtual Environment
Create the environment in the repository root:

bash
python -m venv .venv
Activate it before installing packages.

Windows PowerShell
powershell
.\.venv\Scripts\Activate.ps1
Windows Command Prompt
text
.venv\Scripts\activate.bat
macOS / Linux
bash
source .venv/bin/activate
Then use the VS Code Command Palette to select the project interpreter:

Press Ctrl+Shift+P.

Run Python: Select Interpreter.

Select the interpreter inside .venv.

Verify the active interpreter:

bash
python -c "import sys; print(sys.executable)"
The printed path should contain .venv.

4. Create the Project Structure
Create the following directory and file structure at the repository root:

text
market-data-eda/
├── .github/
│   └── workflows/
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
├── docs/
├── notebooks/
├── scripts/
├── src/
│   └── market_data_eda/
│       ├── __init__.py
│       ├── data_loading.py
│       └── quality_checks.py
├── tests/
│   ├── __init__.py
│   └── test_data_loading.py
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── README.md
├── pyproject.toml
└── requirements-dev.txt
Folder purpose
Path	Purpose
.github/workflows/	GitHub Actions continuous-integration workflows to add later
data/raw/	Original source data; normally excluded from Git if files are large or restricted
data/processed/	Derived/cleaned data; usually reproducible and often excluded from Git
data/sample/	Small, non-sensitive sample datasets that can be committed for reproducible demos/tests
docs/	Project notes, data dictionary, methodology, and decisions
notebooks/	Exploratory notebooks; keep reusable production code in src/
scripts/	Runnable command-line scripts, such as data ingestion or report generation
src/market_data_eda/	Importable application/package code
tests/	Automated tests for reusable code
Recommended terminal commands
On macOS/Linux or Git Bash:

bash
mkdir -p .github/workflows data/raw data/processed data/sample docs notebooks scripts src/market_data_eda tests
touch src/market_data_eda/__init__.py
touch src/market_data_eda/data_loading.py
touch src/market_data_eda/quality_checks.py
touch tests/__init__.py
touch tests/test_data_loading.py
touch .env.example .gitignore .pre-commit-config.yaml README.md pyproject.toml requirements-dev.txt
On Windows PowerShell:

powershell
New-Item -ItemType Directory -Force -Path .github/workflows, data/raw, data/processed, data/sample, docs, notebooks, scripts, src/market_data_eda, tests
New-Item -ItemType File -Force -Path src/market_data_eda/__init__.py, src/market_data_eda/data_loading.py, src/market_data_eda/quality_checks.py, tests/__init__.py, tests/test_data_loading.py, .env.example, .gitignore, .pre-commit-config.yaml, README.md, pyproject.toml, requirements-dev.txt
5. Configure pyproject.toml
Paste the following content into pyproject.toml:

text
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "ai-engineering-foundations"
version = "0.1.0"
description = "AI engineering learning projects and production-minded Python practice"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "numpy>=1.26",
    "pandas>=2.2",
    "matplotlib>=3.8",
    "seaborn>=0.13",
]

[project.optional-dependencies]
dev = [
    "jupyter>=1.0",
    "pytest>=8.0",
    "ruff>=0.6",
    "black>=24.0",
    "pre-commit>=3.7",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-ra -q"

[tool.ruff]
line-length = 88
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I", "B"]

[tool.black]
line-length = 88
target-version = ["py311"]
Important naming correction
The supplied package metadata uses the name ai-engineering-foundations, while this repository is named market-data-eda. For a focused and professional portfolio repository, these names should match. Use this recommended version instead:

text
[project]
name = "market-data-eda"
version = "0.1.0"
description = "Exploratory data analysis and data-quality checks for market datasets"
readme = "README.md"
requires-python = ">=3.11"
Keep the rest of the supplied configuration unchanged. The install command works with either metadata name because it installs the project from the current directory.

6. Install Project and Development Dependencies
With the virtual environment activated, upgrade pip and install the project in editable mode with its development dependencies:

bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
The -e option means editable install. Python imports the package from the current repository, so changes in src/market_data_eda/ are available immediately without reinstalling the package.

The .[dev] syntax means:

.: install the project in the current directory

[dev]: also install the dev dependency group defined in pyproject.toml

This installs the analysis libraries (numpy, pandas, matplotlib, seaborn) and development tools (jupyter, pytest, ruff, black, pre-commit).

Check that the tools are available:

bash
python -m pytest --version
ruff --version
black --version
pre-commit --version
7. Configure Git Ignore Rules
Add this baseline content to .gitignore:

text
# Virtual environments
.venv/
venv/

# Python cache, build, and package artifacts
__pycache__/
*.py[cod]
*.egg-info/
build/
dist/

# Test, coverage, lint, and notebook cache
.pytest_cache/
.coverage
htmlcov/
.ruff_cache/
.ipynb_checkpoints/

# Environment variables and secrets
.env

# Large or local datasets
/data/raw/*
/data/processed/*

# Keep directory structure and safe samples visible in Git
!/data/raw/.gitkeep
!/data/processed/.gitkeep
!/data/sample/

# Operating system and editor files
.DS_Store
.vscode/
Create empty placeholder files so ignored data directories are retained in Git:

bash
# macOS/Linux/Git Bash
touch data/raw/.gitkeep data/processed/.gitkeep
powershell
# Windows PowerShell
New-Item -ItemType File -Force -Path data/raw/.gitkeep, data/processed/.gitkeep
Do not add API tokens or private credentials to .env.example. It should contain only placeholder variable names, for example:

text
# Copy to .env and set local values. Do not commit .env.
MARKET_DATA_API_KEY=replace_with_your_key
8. Configure Pre-commit
Create .pre-commit-config.yaml with the following content:

text
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.16.8
    hooks:
      - id: ruff-check
        args: [--fix]
      - id: ruff-format
The URLs above must be plain YAML strings. Do not paste Markdown link syntax such as [text](url) into a YAML file.

Although pre-commit is declared in the dev dependency group, it still needs to register Git hooks locally. Run both commands after installation:

bash
pre-commit install
pre-commit run --all-files
Why both commands are necessary:

pre-commit install installs a Git hook in .git/hooks/. From then on, checks run automatically before each commit.

pre-commit run --all-files runs the configured hooks against the repository now. It catches formatting, whitespace, YAML, or file-size problems before the first commit.

If a hook modifies files, inspect the changes and stage them again:

bash
git status
git add .
9. Add Minimal Starter Code
Add a small importable function so the initial structure includes executable, tested code.

Create src/market_data_eda/data_loading.py:

python
"""Utilities for loading market-data files."""

from pathlib import Path

import pandas as pd


def load_csv(path: Path) -> pd.DataFrame:
    """Load a CSV file after confirming that it exists."""
    if not path.is_file():
        raise FileNotFoundError(f"CSV file not found: {path}")

    return pd.read_csv(path)
Create src/market_data_eda/quality_checks.py:

python
"""Data-quality checks for market-data datasets."""

import pandas as pd


def missing_value_counts(data: pd.DataFrame) -> pd.Series:
    """Return the missing-value count for each column."""
    return data.isna().sum()
Create tests/test_data_loading.py:

python
from pathlib import Path

import pandas as pd
import pytest

from market_data_eda.data_loading import load_csv


def test_load_csv_reads_data(tmp_path: Path) -> None:
    csv_path = tmp_path / "prices.csv"
    pd.DataFrame({"close": [100.0, 101.5]}).to_csv(csv_path, index=False)

    result = load_csv(csv_path)

    assert result["close"].tolist() == [100.0, 101.5]


def test_load_csv_raises_for_missing_file(tmp_path: Path) -> None:
    missing_path = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError, match="CSV file not found"):
        load_csv(missing_path)
Run the baseline quality checks:

bash
ruff check .
black --check .
pytest
If Black reports formatting changes, apply them and rerun the checks:

bash
black .
ruff check . --fix
pre-commit run --all-files
pytest
10. Make the First Commit
Before starting any analysis, inspect exactly what will be committed:

bash
git status
git diff --cached
Stage the initial repository setup:

bash
git add .
Run the pre-commit checks one more time:

bash
pre-commit run --all-files
Commit the bootstrap work:

bash
git commit -m "chore: initialize market data EDA project"
Push the first commit to GitHub:

bash
git push -u origin main
If your default branch is named master, use this instead:

bash
git push -u origin master
Definition of Done
The bootstrap is complete when all statements below are true:

The market-data-eda repository exists on GitHub and is cloned locally through VS Code.

VS Code uses the repository’s .venv Python interpreter.

The directory layout matches the documented structure.

pyproject.toml defines runtime and development dependencies.

python -m pip install -e ".[dev]" completes successfully.

.gitignore excludes .venv, .env, cache files, and non-sample raw/processed data.

.pre-commit-config.yaml has valid YAML and pre-commit install has completed.

pre-commit run --all-files passes, or all hook modifications have been staged and rerun.

ruff check ., black --check ., and pytest pass.

The first commit uses chore: initialize market data EDA project.

The initial commit is pushed to GitHub.

Next Project Rule
Make a small, meaningful commit before each new piece of work: data ingestion, validation rules, an EDA notebook, a chart, documentation, a test, or CI. This creates a visible engineering history and makes the project easier to review in a portfolio.
