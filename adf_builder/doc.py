from .base import TopLevelNode


class ADFDocument:

    def __init__(self, *args: TopLevelNode):
        self._payload: dict = {
            "version": 1,
            "type": "doc",
        }
        self._content = []
        for provided_arg in args:
            self._content.append(
                provided_arg
            )

    def add(self, node: TopLevelNode):
        self._content.append(node)

    def build(self):
        payload = self._payload.copy()
        json_content = []
        for node in self._content:
            json_content.append(
                node.to_dict()
            )
        payload["content"] = json_content
        return payload
