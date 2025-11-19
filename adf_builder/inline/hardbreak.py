from adf_builder.base import InlineNode


class HardBreak(InlineNode):

    def __init__(self):
        self._payload = {
            "type": "hardBreak"
        }

    def to_dict(self):
        return self._payload
