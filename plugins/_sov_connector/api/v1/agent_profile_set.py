"""POST /api/plugins/_sov_connector/v1/agent_profile_set."""
from __future__ import annotations

import plugins._sov_connector.api.v1.base as connector_base
from helpers.api import Request, Response


class AgentProfileSet(connector_base.ProtectedConnectorApiHandler):
    async def process(self, input: dict, request: Request) -> dict | Response:
        from api.agent_profile_set import SetAgentProfile

        handler = SetAgentProfile(self.app, self.thread_lock)
        return await handler.process(input, request)
