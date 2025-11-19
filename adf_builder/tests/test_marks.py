from adf_builder.marks import MarkEnum, Link, Color


class TestMarks:


    def test_to_json(self):
        assert MarkEnum.CODE.to_dict() == {"type": "code"}
        assert MarkEnum.BOLD.to_dict() == {"type": "strong"}
        assert MarkEnum.ITALIC.to_dict() == {"type": "em"}
        assert MarkEnum.STRIKETHROUGH.to_dict() == {"type": "strike"}
        assert MarkEnum.SUPERSCRIPT.to_dict() == {"type": "subsup", "attrs": {"type": "sup"}}
        assert MarkEnum.SUBSCRIPT.to_dict() == {"type": "subsup", "attrs": {"type": "sub"}}
        assert MarkEnum.UNDERLINE.to_dict() == {"type": "underline"}
        assert Link(title="Test", href="example.com").to_dict() == {
            "type": "link",
            "attrs": {
                "href": "example.com",
                "title": "Test"
            }
        }
        assert Color("#FFFFFF").to_dict() == {
            "type": "textColor",
            "attrs": {
                "color": "#FFFFFF"
            }
        }
