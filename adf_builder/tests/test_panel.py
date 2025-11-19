from adf_builder.inline.text import Text
from adf_builder.top.panel import Panel, PanelType
from adf_builder.top.paragraph import Paragraph
from adf_builder.top.list import BulletList


class TestPanel:

    def test_simple_panel(self):
        assert Panel(
            Paragraph(
                Text(
                    "Simple string"
                )
            ),
            panel_type=PanelType.INFO
        ).to_dict() == {
            "type": "panel",
            "attrs": {
                "panelType": "info"
            },
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "Simple string"
                        }
                    ]
                }
            ]
        }

    def test_list_panel(self):
        assert Panel(
            BulletList(
                Text("foo"),
                BulletList(
                    Text("bar")
                ),
                Text("foo")
            ),
            panel_type=PanelType.WARNING
        ).to_dict() == {
            "type": "panel",
            "attrs": {
                "panelType": "warning"
            },
            "content": [
                {
                    "type": "bulletList",
                    "content": [
                        {
                            "type": "listItem",
                            "content": [
                                {
                                    "type": "paragraph",
                                    "content": [
                                        {
                                            "type": "text",
                                            "text": "foo"
                                        }
                                    ]
                                },
                                {
                                    "type": "bulletList",
                                    "content": [
                                        {
                                            "type": "listItem",
                                            "content": [
                                                {
                                                    "type": "paragraph",
                                                    "content": [
                                                        {
                                                            "type": "text",
                                                            "text": "bar"
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "listItem",
                            "content": [
                                {
                                    "type": "paragraph",
                                    "content": [
                                        {
                                            "type": "text",
                                            "text": "foo"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
