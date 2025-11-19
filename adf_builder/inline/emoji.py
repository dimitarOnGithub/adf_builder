from adf_builder.base import InlineNode


class Emoji(InlineNode):

    def __init__(self, emoji_name: str):
        self._payload = {
            "type": "emoji",
            "attrs": {
                "shortName": emoji_name,
            }
        }

    def to_dict(self):
        return self._payload
