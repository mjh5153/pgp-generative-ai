"""Small deterministic text utilities for offline examples."""


def count_words(text: str) -> str:
    """Return the whitespace-delimited word count as text for tool results."""
    return str(len(text.split()))
