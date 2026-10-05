"""Environment-backed configuration for local demos."""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class AgentConfig:
    max_steps: int = 3


def load_agent_config() -> AgentConfig:
    """Load and validate the sample agent's bounded-loop configuration."""
    raw_max_steps = os.environ.get("CLASS_DEMOS_AGENT_MAX_STEPS", "3")
    try:
        max_steps = int(raw_max_steps)
    except ValueError as error:
        raise ValueError("CLASS_DEMOS_AGENT_MAX_STEPS must be an integer") from error
    if max_steps < 1:
        raise ValueError("CLASS_DEMOS_AGENT_MAX_STEPS must be at least 1")
    return AgentConfig(max_steps=max_steps)
