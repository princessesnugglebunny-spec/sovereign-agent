from typing import Any

from agent import LoopData
from helpers import plugins
from helpers.extension import Extension

TOOL_KWARGS_KEY = "_tool_prompt_kwargs"


class TextEditorConfig(Extension):

    async def execute(
        self,
        system_prompt: list[str] = [],
        loop_data: LoopData = LoopData(),
        **kwargs: Any,
    ):
        if not self.agent:
            return
        config = plugins.get_plugin_config("_text_editor", agent=self.agent) or {}
        tool_kwargs = self.agent.data.setdefault(TOOL_KWARGS_KEY, {})
        tool_kwargs["agent.system.tool.text_editor.md"] = {
            "default_line_count": config.get("default_line_count", 100),
        }
