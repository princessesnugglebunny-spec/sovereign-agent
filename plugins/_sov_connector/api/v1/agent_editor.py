"""POST /api/plugins/_sov_connector/v1/agent_editor."""
from __future__ import annotations

import plugins._sov_connector.api.v1.base as connector_base
from helpers.api import Request, Response


class AgentEditor(connector_base.ProtectedConnectorApiHandler):
    async def process(self, input: dict, request: Request) -> dict | Response:
        from plugins._agent_editor.api.agent_editor import (
            AgentEditor as CoreAgentEditor,
        )

        handler = CoreAgentEditor(self.app, self.thread_lock)
        return await handler.process(input, request)
