from adf_builder.base import TopLevelNode
from .code import CodeBlock
from .paragraph import Paragraph
from .list import BulletList, OrderedList


class Quote(TopLevelNode):

    def __init__(self, *args: Paragraph | BulletList | OrderedList | CodeBlock):
        super().__init__()
        self._payload = {
            "type": "blockquote"
        }
        for inline_node in args:
            if not isinstance(inline_node, (Paragraph, BulletList, OrderedList, CodeBlock)):
                raise ValueError("Quote blocks only accept paragraphs, lists or code blocks")
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
