import pytest
from adf_builder.inline.text import Text
from adf_builder.top.quote import Quote
from adf_builder.top.paragraph import Paragraph
from adf_builder.top.heading import Heading


class TestQuote:

    def test_simple_quote(self):
        assert Quote(
            Paragraph(
                Text("A simple quote")
            )
        ).to_dict() == {
            "type": "blockquote",
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "A simple quote"
                        }
                    ]
                }
            ]
        }

    def test_multiline_quote(self):
        assert Quote(
            Paragraph(
                Text(
                    "Line one"
                )
            ),
            Paragraph(
                Text(
                    "Line two"
                )
            )
        ).to_dict() == {
            "type": "blockquote",
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "Line one"
                        }
                    ]
                },
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "Line two"
                        }
                    ]
                }
            ]
        }

    def test_disallowed_quote(self):
        with pytest.raises(ValueError):
            Quote(
                Heading(
                    Text("This shouldn't work"),
                    level=1
                )
            )