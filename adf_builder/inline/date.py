from adf_builder.base import InlineNode
from datetime import datetime


class Timestamp(InlineNode):

    def __init__(self, time_object: datetime):
        self._payload = {
            "type": "date",
            "attrs": {
                "timestamp": time_object.timestamp()
            }
        }

    def to_dict(self):
        return self._payload
