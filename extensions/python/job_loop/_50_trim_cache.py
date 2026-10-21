from typing import Any

from helpers import cache
from helpers.extension import Extension


class SaveToolCallFile(Extension):
    def execute(self, data: dict[str, Any] | None = None, **kwargs):
        # trim unused cache entries
        cache.trim_cache("*", seconds=300)
