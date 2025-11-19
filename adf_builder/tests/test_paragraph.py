from adf_builder.inline.text import Text
from adf_builder.marks import MarkEnum, Color, Link
from adf_builder.top.paragraph import Paragraph


class TestParagraph:

    def test_basic_paragraph(self):
        ...

    def test_formatted_paragraph(self):
        assert Paragraph(
            Text("A "),
            Text("sentence").mark(MarkEnum.BOLD),
            Text(" "),
            Text("with").mark(MarkEnum.ITALIC),
            Text(" "),
            Text("a lot ").mark(MarkEnum.UNDERLINE),
            Text("of different").mark(Color("#ff5630")),
            Text(" "),
            Text("formatting options").mark(MarkEnum.CODE),
            Text(" "),
            Text("applied ").mark(Link(href="http://example.com")),
            Text("to it.").mark(MarkEnum.SUPERSCRIPT)
        ).to_dict() == {
            "type": "paragraph",
            "content": [
                {
                    "type": "text",
                    "text": "A "
                },
                {
                    "type": "text",
                    "text": "sentence",
                    "marks": [
                        {
                            "type": "strong"
                        }
                    ]
                },
                {
                    "type": "text",
                    "text": " "
                },
                {
                    "type": "text",
                    "text": "with",
                    "marks": [
                        {
                            "type": "em"
                        }
                    ]
                },
                {
                    "type": "text",
                    "text": " "
                },
                {
                    "type": "text",
                    "text": "a lot ",
                    "marks": [
                        {
                            "type": "underline"
                        }
                    ]
                },
                {
                    "type": "text",
                    "text": "of different",
                    "marks": [
                        {
                            "type": "textColor",
                            "attrs": {
                                "color": "#ff5630"
                            }
                        }
                    ]
                },
                {
                    "type": "text",
                    "text": " "
                },
                {
                    "type": "text",
                    "text": "formatting options",
                    "marks": [
                        {
                            "type": "code"
                        }
                    ]
                },
                {
                    "type": "text",
                    "text": " "
                },
                {
                    "type": "text",
                    "text": "applied ",
                    "marks": [
                        {
                            "type": "link",
                            "attrs": {
                                "href": "http://example.com"
                            }
                        }
                    ]
                },
                {
                    "type": "text",
                    "text": "to it.",
                    "marks": [
                        {
                            "type": "subsup",
                            "attrs": {
                                "type": "sup"
                            }
                        }
                    ]
                }
            ]
        }
