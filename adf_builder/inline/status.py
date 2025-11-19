from adf_builder.base import InlineNode


class Status(InlineNode):

    def __init__(self, text: str, color: str):
        self._payload = {
            "type": "status",
            "attrs": {
                "text": text,
                "color": color
            }
        }

    def to_dict(self):
        return self._payload
