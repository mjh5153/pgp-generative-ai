# Importing a Colab demo

1. In Colab, download the notebook as an `.ipynb` file and place it in `notebooks/class_demos/`.
2. Open it in VS Code. Install the `notebooks` group with `uv sync --locked --group notebooks`, then select the repository's `.venv` Python interpreter as the notebook kernel.
3. Migrate Colab-specific code in a working copy: replace `google.colab` imports, `drive.mount()`, `/content` paths, and notebook shell installation commands such as `!pip install` with local equivalents. Keep the downloaded source intact when changing it would alter the instructional meaning.
4. For Google Drive inputs, download an approved copy yourself or configure a local path. Do not assume Drive is mounted or a Google account is connected. Keep private data outside version control and document the expected input without committing it.
5. Resolve data paths from the installed local package location so they do not depend on the notebook's current working directory:

   ```python
   from pathlib import Path

   import class_demos_ai

   REPO_ROOT = Path(class_demos_ai.__file__).resolve().parents[2]
   sample_path = REPO_ROOT / "data" / "sample" / "your_file.csv"
   ```

   This assumes the repository environment has been installed with `uv sync`; the editable package location anchors paths at the checkout.
6. Move reusable logic into `src/class_demos_ai/` and leave the notebook focused on explanation, exploration, and calling package code.
7. Add required packages to the narrowest suitable `pyproject.toml` dependency group and regenerate the lock with `uv lock`. Avoid notebook-local installation commands so setup is reproducible.
8. Clear stale or bulky cell outputs when appropriate, while retaining outputs needed to teach the demo. Inspect notebook diffs and check every cell and output for API keys, tokens, personal data, and private dataset contents before committing.
9. Treat notebook runs as exploratory. Put repeatable behavior in scripts and automated checks in `tests/`; do not treat a successful interactive run as a test.