"""A bounded tool loop with a deterministic mock model."""

import logging
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import Protocol

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class ToolCall:
    name: str
    arguments: Mapping[str, str]


@dataclass(frozen=True)
class FinalAnswer:
    text: str


AgentAction = ToolCall | FinalAnswer
ToolHandler = Callable[[str], str]


@dataclass(frozen=True)
class ToolResult:
    name: str
    output: str | None = None
    error: str | None = None


@dataclass(frozen=True)
class AgentResult:
    answer: str
    steps: int


class Model(Protocol):
    """Small boundary where a real model adapter can be added later."""

    def next_action(
        self, prompt: str, tool_results: tuple[ToolResult, ...]
    ) -> AgentAction: ...


class AgentStepLimitError(RuntimeError):
    """Raised when the model does not finish within the configured bound."""


class MockModel:
    """Deterministically request word count, then return a canned response."""

    def next_action(
        self, prompt: str, tool_results: tuple[ToolResult, ...]
    ) -> AgentAction:
        if not tool_results:
            return ToolCall(name="count_words", arguments={"text": prompt})
        result = tool_results[-1]
        if result.error is not None:
            return FinalAnswer("The local word-count tool failed safely.")
        return FinalAnswer(f"The local word-count tool counted {result.output} words.")


def run_agent(
    prompt: str,
    model: Model,
    tools: Mapping[str, ToolHandler],
    max_steps: int = 3,
) -> AgentResult:
    """Run a model/tool loop with a strict maximum number of model actions."""
    if max_steps < 1:
        raise ValueError("max_steps must be at least 1")

    tool_results: list[ToolResult] = []
    for step in range(1, max_steps + 1):
        action = model.next_action(prompt, tuple(tool_results))
        if isinstance(action, FinalAnswer):
            return AgentResult(answer=action.text, steps=step)

        tool = tools.get(action.name)
        if tool is None:
            tool_results.append(ToolResult(name=action.name, error="UnknownToolError"))
            logger.warning(
                "Tool failed: name=%s step=%d error_type=unknown", action.name, step
            )
            continue

        try:
            output = tool(action.arguments.get("text", ""))
        except Exception as error:
            tool_results.append(
                ToolResult(name=action.name, error=type(error).__name__)
            )
            logger.warning(
                "Tool failed: name=%s step=%d error_type=%s",
                action.name,
                step,
                type(error).__name__,
            )
        else:
            tool_results.append(ToolResult(name=action.name, output=output))
            logger.info("Tool completed: name=%s step=%d", action.name, step)

    raise AgentStepLimitError(f"Agent reached the maximum of {max_steps} steps")
