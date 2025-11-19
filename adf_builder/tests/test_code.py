import pytest
from adf_builder.marks import MarkEnum
from adf_builder.top.code import CodeBlock
from adf_builder.top.paragraph import Paragraph
from adf_builder.inline.text import Text


class TestCodeBlock:


    def test_constructor(self):
        block = CodeBlock("This is a test string!")
        assert block.to_dict() == {
            "type": "codeBlock",
            "attrs": {
                "language": "text"
            },
            "content": [
                {
                    "type": "text",
                    "text": "This is a test string!"
                }
            ]
        }

    def test_invalid_content(self):
        with pytest.raises(ValueError):
            CodeBlock(
                Text("This is a test string!").mark(MarkEnum.BOLD)
            )
        with pytest.raises(ValueError):
            CodeBlock(
                Paragraph(

                )
            )
