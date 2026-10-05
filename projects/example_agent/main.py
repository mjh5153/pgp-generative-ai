"""Runnable entry point for the offline orchestration demo."""

import logging

from class_demos_ai.agents import MockModel, run_agent
from class_demos_ai.config import load_agent_config
from class_demos_ai.tools import count_words


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    config = load_agent_config()
    result = run_agent(
        prompt="Count the words in this example request.",
        model=MockModel(),
        tools={"count_words": count_words},
        max_steps=config.max_steps,
    )
    print(result.answer)


if __name__ == "__main__":
    main()
