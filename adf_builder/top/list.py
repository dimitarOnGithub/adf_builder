from adf_builder.base import TopLevelNode
from adf_builder.inline.text import Text
from .code import CodeBlock
from .paragraph import Paragraph


class _ListItem:

    def __init__(self, item: CodeBlock | Text):
        super().__init__()
        self._payload = {
            "type": "listItem"
        }
        if isinstance(item, Text):
            item = Paragraph(item)
        self._content = [item]

    def to_dict(self):
        payload = self._payload.copy()
        json_content = []
        for node in self._content:
            json_content.append(
                node.to_dict()
            )
        payload["content"] = json_content
        return payload

    def add_nested(self, content: 'BulletList | OrderedList') -> None:
        self._content.append(content)


class _List(TopLevelNode):

    def __init__(self, *items: 'CodeBlock | Text | BulletList | OrderedList'):
        super().__init__()
        _last_item = None
        self.depth = 0
        for provided_arg in items:
            if isinstance(provided_arg, BulletList | OrderedList):
                if _last_item is None:
                    raise ValueError("Nested lists require at least one text or code block entry to their parent list "
                                     "before another list can be nested")
                if self.depth + provided_arg.depth >= 5:
                    raise ValueError(f"Maximum nesting exceeded at list: {provided_arg}")
                self.depth += provided_arg.depth + 1
                _last_item.add_nested(provided_arg)
                continue
            list_item = _ListItem(provided_arg)
            self._content.append(list_item)
            _last_item = list_item

    def to_dict(self):
        payload = self._payload.copy()
        json_content = []
        for node in self._content:
            json_content.append(
                node.to_dict()
            )
        payload["content"] = json_content
        return payload


class BulletList(_List):

    def __init__(self, *items: 'CodeBlock | Text | BulletList | OrderedList'):
        super().__init__(*items)
        self._payload = {
            "type": "bulletList"
        }


class OrderedList(_List):

    def __init__(self, *items: 'CodeBlock | Text | BulletList | OrderedList', start_at=1):
        super().__init__(*items)
        self._payload = {
            "type": "orderedList",
            "attrs": {
                "order": start_at
            },
        }
