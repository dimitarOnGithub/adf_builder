from adf_builder.doc import ADFDocument
from adf_builder.inline.text import Text
from adf_builder.marks import MarkEnum, Color
from adf_builder.top.paragraph import Paragraph
from adf_builder.top.heading import Heading
from adf_builder.top.code import CodeBlock
from adf_builder.top.panel import Panel, PanelType
from adf_builder.top.divider import Divider


class TestADFDocument:


    def test_creation(self):
        payload = ADFDocument().build()
        assert payload.get('version') == 1
        assert payload.get('type') == 'doc'
        assert payload.get('content') == []

    def test_simple_doc(self):
        doc = ADFDocument(
            Paragraph(
                Text(
                    "This is a test string!"
                )
            )
        )
        assert doc.build() == {
            "version": 1,
            "type": "doc",
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "This is a test string!"
                        }
                    ]
                }
            ]
        }

    def test_formatted_doc(self):
        formatted_doc = ADFDocument(
            Paragraph(
                Text(
                    "A "
                ),
                Text("simple").mark(MarkEnum.BOLD),
                Text(
                    " text string!"
                )
            )
        )
        assert formatted_doc.build() == {
            "version": 1,
            "type": "doc",
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "A "
                        },
                        {
                            "type": "text",
                            "text": "simple",
                            "marks": [
                                {
                                    "type": "strong"
                                }
                            ]
                        },
                        {
                            "type": "text",
                            "text": " text string!"
                        }
                    ]
                }
            ]
        }

    def test_build(self):
        assert ADFDocument(
            Heading(
                Text("Test Results"),
                level=1
            ),
            Divider(),
            Heading(
                Text("Test One"),
                level=3
            ),
            Paragraph(
                Text("Test was successful").mark(MarkEnum.ITALIC)
            ),
            CodeBlock("package foo.bar;\n\npublic class Foobar {\n  private int foo;\n}", language="java"),
            Divider(),
            Heading(
                Text("Test Two"),
                level=3
            ),
            Paragraph(
                Text("Test observed "),
                Text("two").mark(MarkEnum.BOLD),
                Text(" "),
                Text("failures").mark(Color("#ff5630"))
            ),
            Divider(),
            Panel(
                Paragraph(
                    Text("Some failures were detected.")
                ),
                panel_type=PanelType.WARNING
            )
        ).build() == {
            "version": 1,
            "type": "doc",
            "content": [
                {
                    "type": "heading",
                    "attrs": {
                        "level": 1
                    },
                    "content": [
                        {
                            "type": "text",
                            "text": "Test Results"
                        }
                    ]
                },
                {
                    "type": "rule"
                },
                {
                    "type": "heading",
                    "attrs": {
                        "level": 3
                    },
                    "content": [
                        {
                            "type": "text",
                            "text": "Test One"
                        }
                    ]
                },
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "Test was successful",
                            "marks": [
                                {
                                    "type": "em"
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "codeBlock",
                    "attrs": {
                        "language": "java"
                    },
                    "content": [
                        {
                            "type": "text",
                            "text": "package foo.bar;\n\npublic class Foobar {\n  private int foo;\n}"
                        }
                    ]
                },
                {
                    "type": "rule"
                },
                {
                    "type": "heading",
                    "attrs": {
                        "level": 3
                    },
                    "content": [
                        {
                            "type": "text",
                            "text": "Test Two"
                        }
                    ]
                },
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "Test observed "
                        },
                        {
                            "type": "text",
                            "text": "two",
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
                            "text": "failures",
                            "marks": [
                                {
                                    "type": "textColor",
                                    "attrs": {
                                        "color": "#ff5630"
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "rule"
                },
                {
                    "type": "panel",
                    "attrs": {
                        "panelType": "warning"
                    },
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": "Some failures were detected."
                                }
                            ]
                        }
                    ]
                }
            ]
        }

    def test_dynamic_doc(self):
        doc = ADFDocument()
        for i in range(1, 4):
            doc.add(
                Paragraph(
                    Text(f"A line of text {i}")
                )
            )
        assert doc.build() == {
            "version": 1,
            "type": "doc",
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "A line of text 1"
                        }
                    ]
                },
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "A line of text 2"
                        }
                    ]
                },
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "A line of text 3"
                        }
                    ]
                }
            ]
        }
