# Path toward production

This repository is a learning and development scaffold, not a production-ready service. Promote a demo only when a concrete application and its users are understood:

1. Extract reusable logic from the notebook into `src/class_demos_ai/` and keep the notebook as an explanatory interface.
2. Validate configuration and inputs; add focused unit tests, integration tests where warranted, and evaluation cases for model behavior.
3. Add a CLI or API only when a specific use case calls for one.
4. For a selected model provider, define timeouts, bounded retries, rate limits, and cost controls appropriate to that provider and workload.
5. Review tool permissions, data handling and retention, prompt-injection risks, and human approval requirements for consequential actions. Keep tools least-privileged and bounded.
6. Once a target environment and operating requirements are selected, add application packaging, deployment configuration, monitoring, and release automation for that target.

A real model adapter belongs behind the `Model` protocol in `src/class_demos_ai/agents/sample.py`; add a provider SDK only in an appropriate optional dependency group after choosing a provider. The current mock is deterministic orchestration scaffolding, not evidence of model quality or production behavior.