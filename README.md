# PGP Generative AI Demos

A workspace for importing class demonstrations, exploring ideas in notebooks, and promoting selected work into reusable Python components. This scaffold is intentionally lightweight: the core package has no runtime dependencies, and optional tooling is installed only when needed. It is not a production-ready application.

## Quick start

Install [uv](https://docs.astral.sh/uv/) first, then run the commands from the repository root.

macOS/Linux:

```sh
uv python install 3.11
uv sync --locked
uv run python projects/example_agent/main.py
```

Windows PowerShell:

```powershell
uv python install 3.11
uv sync --locked
uv run python projects/example_agent/main.py
```

These commands use the project environment directly; shell activation is not required. Optional groups can be added when needed, for example `uv sync --locked --group notebooks`.

## Offline example

Run `uv run python projects/example_agent/main.py`. It sends a deterministic mock action to a harmless local word-count tool and prints a result. The mock demonstrates orchestration only; it does not perform real LLM reasoning or call a provider. Its maximum steps are configurable with `CLASS_DEMOS_AGENT_MAX_STEPS`.

## Notebooks in VS Code

Open this repository folder in VS Code, install the recommended Python, Pylance, Jupyter, and Ruff extensions, and run `uv sync --locked --group notebooks`. Open a notebook under `notebooks/class_demos/`, choose the `.venv` Python interpreter as its kernel, and run cells interactively. Notebook execution is exploratory; use scripts and pytest for repeatable checks.

## Import a Colab demo

Download the notebook as `.ipynb` and follow [the Colab migration guide](docs/importing_colab.md). Keep the downloaded source intact when edits would change its instructional meaning; migrate a working copy instead.

## Dependencies

Add runtime dependencies to `[project].dependencies` only when they are needed by the reusable core. Put optional tooling in the `notebooks`, `agentic`, or `api` dependency groups; put developer tools in `dev`. Then run `uv lock` and commit both `pyproject.toml` and `uv.lock`. Provider SDKs and agent frameworks are not installed by default.

## Quality checks

```sh
uv run ruff check .
uv run ruff format --check .
uv run ty check src tests
uv run pytest
```

## Structure

- `notebooks/class_demos/`: imported and exploratory class notebooks.
- `projects/`: runnable application experiments; `example_agent/` is the offline sample.
- `src/class_demos_ai/`: reusable package code, including agent interfaces and safe local tools.
- `tests/`: repeatable behavior checks.
- `data/sample/`, `data/raw/`, `data/processed/`: small shareable fixtures, original inputs, and generated data. Raw and processed contents are ignored by default.
- `docs/`: migration, local development, and production-readiness guidance.
- `.github/`: CI checks, contribution and Copilot guidance.

## Promote a demo

Start with [the development guide](docs/development.md), then follow the staged path in [production readiness](docs/production_readiness.md). A production target and requirements have not been selected. Choose a license before public distribution; no license is selected or included here.