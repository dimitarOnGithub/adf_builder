from adf_builder.base import InlineNode


class Mention(InlineNode):

    def __init__(self, account_id: str):
        self._payload = {
            "type": "mention",
            "attrs": {
                "id": account_id,
            }
        }

    def to_dict(self):
        return self._payload
