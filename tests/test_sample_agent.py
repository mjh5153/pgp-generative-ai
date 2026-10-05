"""Behavior tests for the offline agent example."""

import pytest

from class_demos_ai.agents import (
    AgentStepLimitError,
    MockModel,
    ToolCall,
    run_agent,
)


class RepeatingToolModel:
    def next_action(self, prompt: str, tool_results: tuple[object, ...]) -> ToolCall:
        return ToolCall(name="repeat", arguments={"text": prompt})


def test_agent_stops_at_configured_step_limit() -> None:
    with pytest.raises(AgentStepLimitError, match="maximum of 2 steps"):
        run_agent(
            prompt="repeat",
            model=RepeatingToolModel(),
            tools={"repeat": lambda text: text},
            max_steps=2,
        )


def test_agent_handles_tool_failure_without_logging_exception_message(
    caplog: pytest.LogCaptureFixture,
) -> None:
    def failing_tool(text: str) -> str:
        raise RuntimeError("sensitive tool detail")

    result = run_agent(
        prompt="count these words",
        model=MockModel(),
        tools={"count_words": failing_tool},
    )

    assert result.answer == "The local word-count tool failed safely."
    assert "RuntimeError" in caplog.text
    assert "sensitive tool detail" not in caplog.text
