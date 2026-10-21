"""POST /api/plugins/_sov_connector/v1/settings_get."""
from __future__ import annotations

import plugins._sov_connector.api.v1.base as connector_base
from helpers.api import Request, Response


class SettingsGet(connector_base.ProtectedConnectorApiHandler):
    async def process(self, input: dict, request: Request) -> dict | Response:
        from helpers import settings

        return dict(settings.convert_out(settings.get_settings()))
