"""POST /api/plugins/_sov_connector/v1/agents_list."""
from __future__ import annotations

import plugins._sov_connector.api.v1.base as connector_base
from helpers.api import Request, Response


class AgentsList(connector_base.ProtectedConnectorApiHandler):
    async def process(self, input: dict, request: Request) -> dict | Response:
        from helpers import subagents

        return {
            "ok": True,
            "data": subagents.get_all_agents_list(),
        }
