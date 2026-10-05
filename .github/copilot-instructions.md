# Repository conventions

- Keep notebooks instructional and move reusable, tested logic into `src/class_demos_ai/`.
- Keep class demos in `notebooks/class_demos/`; name them with a short topic and, when useful, a date or class session.
- Record runtime or development dependencies in `pyproject.toml` and update `uv.lock` with `uv lock`.
- Keep provider SDKs and application frameworks in optional dependency groups. Do not add credentials or assume a provider.
- Never commit `.env` files, credentials, private datasets, or sensitive notebook outputs. Use `.env.example` for non-secret configuration names and placeholder values only.
- Agent loops must have a validated step bound, explicit tool allowlists, and handled tool errors. Do not add autonomous filesystem mutation or consequential actions without an explicit use case and approval design.
- Before submitting changes, run `uv run ruff check .`, `uv run ruff format --check .`, `uv run ty check src tests`, and `uv run pytest`.