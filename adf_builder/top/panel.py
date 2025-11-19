from adf_builder.base import TopLevelNode
from .list import BulletList, OrderedList
from .paragraph import Paragraph
from .heading import Heading
from enum import Enum


class PanelType(Enum):

    INFO = "info"
    NOTE = "note"
    WARNING = "warning"
    SUCCESS = "success"
    ERROR = "error"


class Panel(TopLevelNode):

    def __init__(self, *args: Heading | BulletList | OrderedList | Paragraph, panel_type: PanelType):
        super().__init__()
        self._payload = {
            "type": "panel",
            "attrs": {
                "panelType": panel_type.value
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
