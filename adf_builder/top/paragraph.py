from adf_builder.base import TopLevelNode, InlineNode


class Paragraph(TopLevelNode):

    def __init__(self, *args: InlineNode):
        super().__init__()
        self._payload = {
            "type": "paragraph"
        }
        for inline_node in args:
            self._content.append(
                inline_node
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
