from adf_builder.base import TopLevelNode, InlineNode


class Heading(TopLevelNode):

    def __init__(self, *args: InlineNode, level: int):
        super().__init__()
        if 1 < level and level > 6:
            raise ValueError("Heading level can only be set to a value between 1 and 6")
        self._payload = {
            "type": "heading",
            "attrs": {
                "level": level
            }
        }
        for provided_arg in args:
            self._content.append(
                provided_arg
            )

    def to_dict(self):
        payload = self._payload.copy()
        json_content = []
        for node in self._content:
            json_content.append(
                node.to_dict()
            )
        payload["content"] = json_content
        return payload
