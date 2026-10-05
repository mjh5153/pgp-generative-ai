# Local development

## Environment

Install `uv`, then run `uv python install 3.11` and `uv sync --locked` from the repository root. The `.python-version` file selects the compatibility baseline. Use `uv run ...` for commands so execution does not depend on shell activation.

To add notebook support, run `uv sync --locked --group notebooks`. Install only the optional groups a project needs. The API group currently offers FastAPI as an optional starting point; it does not create an API or prescribe an architecture. The agentic group is intentionally empty while the example uses a built-in deterministic mock.

## Reusable code and checks

Put reusable modules under `src/class_demos_ai/`, with tests under `tests/`. Keep notebooks in `notebooks/class_demos/` and one-off runnable projects under `projects/`. Add dependencies to `pyproject.toml`, run `uv lock`, and commit the updated lockfile.

Run `uv run ruff check .`, `uv run ruff format --check .`, `uv run ty check src tests`, and `uv run pytest`. VS Code tasks provide the same setup, quality, test, and sample-run commands without requiring activation.