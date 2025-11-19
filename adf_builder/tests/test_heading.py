from adf_builder.inline.text import Text
from adf_builder.marks import MarkEnum
from adf_builder.top.heading import Heading


class TestHeading:

    def test_constructor(self):
        assert Heading(
            Text("A simple header"),
            level=1
        ).to_dict() == {
            "type": "heading",
            "attrs": {
                "level": 1
            },
            "content": [
                {
                    "type": "text",
                    "text": "A simple header"
                }
            ]
        }

        assert Heading(
            Text("A simple header"),
            Text(" continued.").mark(MarkEnum.BOLD),
            level=1
        ).to_dict() == {
            "type": "heading",
            "attrs": {
                "level": 1
            },
            "content": [
                {
                    "type": "text",
                    "text": "A simple header"
                },
                {
                    "type": "text",
                    "text": " continued.",
                    "marks": [
                        {
                            "type": "strong"
                        }
                    ]
                }
            ]
        }
