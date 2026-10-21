from helpers.print_style import PrintStyle
from helpers.ws import WsHandler


class WsHello(WsHandler):
    """Simple echo handler used for foundational testing."""

    async def process(self, event: str, data: dict, sid: str) -> dict | None:
        if event != "hello_request":
            return None
        name = data.get("name") or "stranger"
        PrintStyle.info(f"hello_request from {sid} ({name})")
        return {"message": f"Hello, {name}!", "handler": self.identifier}
