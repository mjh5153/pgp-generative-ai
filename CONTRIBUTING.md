# Contributing

- Give notebook demos a short topic-based name, such as `retrieval_basics.ipynb`; include a class date or session only when it helps distinguish versions.
- Put reusable Python logic in `src/class_demos_ai/` and keep notebook cells focused on explanation, exploration, and calling that logic.
- Add dependencies to the narrowest appropriate `pyproject.toml` group, then run `uv lock`. Explain new heavy or provider-specific dependencies in the change.
- Do not commit credentials, `.env` files, private data, or unnecessary notebook outputs.
- Run the lint, formatting, type, and test commands listed in the README before opening a pull request.