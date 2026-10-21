# Sovereign Agent

An open, self-hosted AI agent framework distilled and re-expressed from original
research. Sovereign Agent gives an LLM a full Linux computer: a shell, a browser
with DOM annotation, document cowork, projects, skills, plugins, and a web UI.

## Features

- Agent loop with tool registry and structured tool results.
- Chat and utility models via LiteLLM (OpenAI-compatible and many providers).
- Built-in tools: code/terminal execution, browser automation, document query,
  knowledge base, memory, scheduler, skills, notifications.
- Extension system (Python + WebUI) for lifecycle hooks.
- Web UI (Alpine.js) with chat, file browser, settings, scheduler, plugins.
- MCP server support, A2A, vector search, project management.
- Plugin architecture for bundled and user plugins.

## Run

```bash
python -m pip install -r requirements.txt
python run_ui.py
```

Then open the URL printed at startup.

## Development

```bash
python -m pytest
python -m ruff check .
```

## Safety

Sovereign Agent executes real commands on a real machine. Run it only in an
environment you control (container/VM recommended). Never expose it to untrusted
networks without authentication.

## Origin

This project is an original re-expression of the Agent Zero framework
(`agent0ai/agent-zero` @ `ff2a5b9c9c4e490ba38dd7c313e779510bb2071a`, tag v2.14),
retaining its architectural decisions and behavior while re-expressing all code
in this project's own conventions and naming. See `docs/code-distilling/`.
```

Let me also create docs/code-distilling spec. But first, let me verify tests pass more broadly. Let me run a quick subset of tests (core).<|end|><|start|>start to=bash<|channel|>analysis <|constrain|>xml<|message|><rfl:parameter name="command">
cd /root/projects/sovereign-agent && python -m pytest tests/test_agent_activity.py tests/test_rate_limiter.py tests/test_tool_policy.py 2>&1 | tail -20