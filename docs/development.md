# Development Setup

This project is being converted from research scripts into a reusable Python
library. During that transition, use a dedicated development environment instead
of installing tools into your system Python or conda base environment.

## Why use a dedicated environment?

A dedicated environment keeps this project's dependencies separate from other
projects on your machine. That makes the work easier to reproduce and safer to
change.

## Create a conda environment

From any terminal:

```bash
conda create -n segval-dev python=3.11
conda activate segval-dev
```

Then install the project in editable development mode:

```bash
cd /Users/rosana_eljurdi/Desktop/SegVal_Repo
python -m pip install -e ".[dev]"
```

Editable mode means Python uses the source files in this checkout directly. When
you edit the code, you do not need to reinstall the project.

## Install reporting tools

Some scripts also generate plots, Excel files, and LaTeX tables. Install those
extra dependencies when working on reporting:

```bash
python -m pip install -e ".[dev,reporting]"
```

## Run checks

Run the test suite:

```bash
python -m pytest
```

Run Ruff linting:

```bash
python -m ruff check --output-format=github .
```

Check formatting:

```bash
python -m ruff format --check .
```

## Dependency groups

Dependencies are declared in `pyproject.toml`.

- Runtime dependencies are needed by the code itself.
- Development dependencies are tools for contributors, such as pytest and Ruff.
- Reporting dependencies are only needed for plots, tables, and spreadsheet
  outputs.

The actual `src/segval` package layout will be added in a follow-up issue.
